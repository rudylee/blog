#!/usr/bin/env python3
"""Publish blog posts from an Obsidian folder to this Hugo site.

Usage:
    python3 scripts/publish.py --from ~/Vault/Blog            # export, build, commit, push
    python3 scripts/publish.py --from ~/Vault/Blog --check    # validate only, write nothing
    python3 scripts/publish.py --from ~/Vault/Blog --no-commit  # export + build, review diff yourself

`--from` can also be set with the BLOG_VAULT_DIR environment variable.

Only notes inside the --from folder with `publish: true` are exported, and only
the attachments those notes reference are copied. Nothing else in the vault is
read. The script stops with an error (writing nothing) when a published post:
  * links or embeds a note that is not published, or a file outside the folder
  * is missing title / date / slug, or reuses another post's slug

Conversions (code blocks and inline code are left alone):
  ![[image.png]] / ![[image.png|alt]]   -> ![alt](/attachments/...)
  ![](attachments/x.png) (relative)     -> ![](/attachments/x.png)
  [[Other Post]] / [[Other Post|text]]  -> [text](/<slug of Other Post>/)
  %% Obsidian comments %%               -> removed

content/posts/ and static/attachments/ are owned by this script: they are
rewritten from the vault on every run.

Requires Python 3.11+ and the `hugo` binary (override with --hugo or $HUGO).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO / "content" / "posts"
ATTACH_DIR = REPO / "static" / "attachments"
ATTACH_URL = "/attachments"

# Front matter keys passed to Hugo. Every other Obsidian property is dropped so
# private metadata never reaches the public repo.
HUGO_KEYS = ["title", "date", "lastmod", "slug", "categories", "tags",
             "aliases", "description"]
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif", ".bmp"}
MAX_DELETES = 3

WIKILINK_RE = re.compile(r"(!?)\[\[([^\]\|#^]+)([#^][^\]\|]*)?(?:\|([^\]]*))?\]\]")
# Matches the "](target)" part only, so nested [![](a)](b) links get both targets.
MDLINK_RE = re.compile(r"(\]\()(<[^>]+>|[^)\s]+)((?:\s+\"[^\"]*\")?\))")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(``.*?``|`[^`]*`)")
COMMENT_RE = re.compile(r"%%.*?%%", re.S)


class PublishError(Exception):
    pass


# --------------------------------------------------------------------------
# Front matter (the subset of YAML Obsidian writes for properties)
# --------------------------------------------------------------------------
def parse_scalar(raw):
    raw = raw.strip()
    if raw == "" or raw in ("null", "~"):
        return None
    if raw.startswith('"'):
        return json.loads(raw)
    if raw.startswith("'"):
        return raw[1:-1].replace("''", "'")
    if raw in ("true", "false"):
        return raw == "true"
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        return [parse_scalar(x) for x in inner.split(",")] if inner else []
    return raw


def parse_front_matter(text, where):
    m = re.match(r"---\n(.*?)\n---[ \t]*(?:\n|$)", text, re.S)
    if not m:
        return {}, text
    props, key = {}, None
    for n, line in enumerate(m.group(1).splitlines(), 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s+-\s*(.*)$", line) or re.match(r"^-\s+(.*)$", line)
        if item and key is not None and isinstance(props[key], list):
            props[key].append(parse_scalar(item.group(1)))
            continue
        kv = re.match(r"^([A-Za-z0-9_-]+):(?:\s+(.*))?$", line)
        if not kv:
            raise PublishError(f"{where}:{n}: unsupported property syntax: {line!r}")
        key, value = kv.group(1), (kv.group(2) or "").strip()
        props[key] = [] if value == "" else parse_scalar(value)
    return props, text[m.end():]


def yaml_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}[T\d:.+-]*Z?", value):
        return value
    return json.dumps(str(value), ensure_ascii=False)


def to_yaml(props):
    out = ["---"]
    for key, value in props.items():
        if isinstance(value, list):
            if value:
                out.append(f"{key}:")
                out.extend(f"  - {yaml_value(v)}" for v in value)
        elif value is not None:
            out.append(f"{key}: {yaml_value(value)}")
    out.append("---")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Vault scanning and link resolution
# --------------------------------------------------------------------------
class Vault:
    def __init__(self, root: Path):
        self.root = root
        self.notes = {}        # path -> (props, body)
        self.published = {}    # path -> slug
        self.files = [p for p in root.rglob("*")
                      if p.is_file() and not any(part.startswith(".")
                                                 for part in p.relative_to(root).parts)]
        for p in self.files:
            if p.suffix == ".md":
                self.notes[p] = parse_front_matter(p.read_text(encoding="utf-8"),
                                                   p.relative_to(root))
                if self.notes[p][0].get("publish") is True:
                    self.published[p] = self.notes[p][0].get("slug")

    def resolve_wiki(self, target, note):
        """Obsidian-style lookup: exact relative path, else unique file name."""
        target = target.strip()
        candidates = [target, target + ".md"]
        for c in candidates:
            for base in (note.parent, self.root):
                p = (base / c).resolve()
                if p.is_file() and p.is_relative_to(self.root):
                    return p
        matches = [p for p in self.files
                   if p.name in candidates or p.relative_to(self.root).as_posix() in candidates
                   or p.relative_to(self.root).as_posix().endswith("/" + target)
                   or p.relative_to(self.root).as_posix().endswith("/" + target + ".md")]
        if len(matches) > 1:
            raise PublishError(f"{self.rel(note)}: [[{target}]] is ambiguous: "
                               + ", ".join(self.rel(m) for m in matches))
        return matches[0] if matches else None

    def rel(self, p):
        return p.relative_to(self.root).as_posix()


def attachment_url(vault, path, assets):
    rel = vault.rel(path)
    if rel.startswith("attachments/"):
        rel = rel[len("attachments/"):]
    rel = "/".join(re.sub(r"\s+", "-", part) for part in rel.split("/"))
    if assets.get(rel, path) != path:
        raise PublishError(f"two attachments map to {rel}: {vault.rel(assets[rel])}, {vault.rel(path)}")
    assets[rel] = path
    return f"{ATTACH_URL}/{rel}"


def convert_body(vault, note, body, assets):
    where = vault.rel(note)

    def link_to(path, label_for_error):
        if path is None:
            raise PublishError(f"{where}: link target not found: {label_for_error}")
        if path.suffix == ".md":
            if path not in vault.published:
                raise PublishError(f"{where}: links to unpublished note "
                                   f"{vault.rel(path)} (publish it or remove the link)")
            return f"/{vault.published[path].strip('/')}/"
        return attachment_url(vault, path, assets)

    def wiki(m):
        embed, target, _anchor, alias = m.groups()
        path = vault.resolve_wiki(target, note)
        url = link_to(path, f"[[{target}]]")
        if embed:
            if path.suffix.lower() in IMAGE_EXT:
                alt = "" if alias is None or re.fullmatch(r"\d+(x\d+)?", alias) else alias
                return f"![{alt}]({url})"
            if path.suffix == ".md":
                raise PublishError(f"{where}: note embeds (![[{target}]]) are not supported")
            return f"[{alias or path.name}]({url})"
        return f"[{alias or target.split('/')[-1]}]({url})"

    def mdlink(m):
        pre, target, post = m.groups()
        raw = target[1:-1] if target.startswith("<") else target
        if re.match(r"^([a-z][a-z0-9+.-]*:|/|#)", raw, re.I):
            return m.group(0)  # external URL, site-absolute path or anchor
        path_part = unquote(raw.split("#")[0])
        p = (note.parent / path_part).resolve()
        if not p.is_relative_to(vault.root):
            raise PublishError(f"{where}: link points outside the blog folder: {raw}")
        return pre + link_to(p if p.is_file() else None, raw) + post

    def convert_text(text):
        text = WIKILINK_RE.sub(wiki, text)
        return MDLINK_RE.sub(mdlink, text)

    body = strip_comments(body)
    out, fence = [], None
    for line in body.split("\n"):
        f = FENCE_RE.match(line)
        if fence:
            out.append(line)
            if f and f.group(1)[0] == fence[0] and len(f.group(1)) >= len(fence):
                fence = None
            continue
        if f:
            fence = f.group(1)
            out.append(line)
            continue
        parts = INLINE_CODE_RE.split(line)
        out.append("".join(p if i % 2 else convert_text(p) for i, p in enumerate(parts)))
    return "\n".join(out)


def strip_comments(body):
    # Only outside fenced code blocks.
    chunks = re.split(r"(^ {0,3}(?:`{3,}|~{3,})[^\n]*\n.*?^ {0,3}(?:`{3,}|~{3,})[ \t]*$)",
                      body, flags=re.S | re.M)
    return "".join(c if i % 2 else COMMENT_RE.sub("", c) for i, c in enumerate(chunks))


# --------------------------------------------------------------------------
# Export
# --------------------------------------------------------------------------
def build_export(vault_dir: Path):
    vault = Vault(vault_dir)
    if not vault.published:
        raise PublishError(f"no notes with `publish: true` found in {vault_dir}")

    posts, assets, slugs, errors = {}, {}, {}, []
    for note, slug in sorted(vault.published.items()):
        props, body = vault.notes[note]
        where = vault.rel(note)
        try:
            for key in ("title", "date", "slug"):
                if not props.get(key):
                    raise PublishError(f"{where}: missing `{key}` property")
            slug = str(slug).strip("/")
            if slug in slugs:
                raise PublishError(f"{where}: slug {slug!r} already used by {slugs[slug]}")
            slugs[slug] = where
            front = {k: props[k] for k in HUGO_KEYS if props.get(k) not in (None, [], "")}
            front["slug"] = slug
            name = slug.rsplit("/", 1)[-1] + ".md"
            if name in posts:
                name = slug.replace("/", "-") + ".md"
            posts[name] = to_yaml(front) + "\n" + convert_body(vault, note, body, assets).lstrip("\n")
        except PublishError as e:
            errors.append(str(e))
    if errors:
        raise PublishError("\n".join(f"  - {e}" for e in errors))
    return posts, assets


def write_export(posts, assets):
    existing = {p.name for p in POSTS_DIR.glob("*.md")}
    removed = sorted(existing - posts.keys())
    for p in POSTS_DIR.glob("*.md"):
        p.unlink()
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    for name, text in posts.items():
        (POSTS_DIR / name).write_text(text, encoding="utf-8")
    if ATTACH_DIR.exists():
        shutil.rmtree(ATTACH_DIR)
    for rel, src in assets.items():
        dest = ATTACH_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    return removed


def run(cmd, **kw):
    print("$", " ".join(str(c) for c in cmd))
    subprocess.run(cmd, cwd=REPO, check=True, **kw)


def git_out(*args):
    return subprocess.run(["git", *args], cwd=REPO, check=True,
                          capture_output=True, text=True).stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="src", type=Path, default=os.environ.get("BLOG_VAULT_DIR"),
                    help="Obsidian blog folder (default: $BLOG_VAULT_DIR)")
    ap.add_argument("--check", action="store_true", help="validate only, write nothing")
    ap.add_argument("--no-commit", action="store_true", help="export and build, but do not commit or push")
    ap.add_argument("--no-push", action="store_true", help="commit but do not push")
    ap.add_argument("--allow-deletes", action="store_true",
                    help=f"allow removing more than {MAX_DELETES} existing posts")
    ap.add_argument("--hugo", default=os.environ.get("HUGO", "hugo"), help="hugo binary")
    args = ap.parse_args()
    if not args.src:
        ap.error("--from (or BLOG_VAULT_DIR) is required")
    src = Path(args.src).expanduser().resolve()
    if not src.is_dir():
        ap.error(f"{src} is not a directory")

    try:
        posts, assets = build_export(src)
    except PublishError as e:
        sys.exit(f"Nothing was written. Fix these first:\n{e}")
    print(f"{len(posts)} published posts, {len(assets)} attachments")

    to_remove = sorted({p.name for p in POSTS_DIR.glob("*.md")} - posts.keys())
    if len(to_remove) > MAX_DELETES and not args.allow_deletes:
        sys.exit(f"This would delete {len(to_remove)} existing posts "
                 f"(e.g. {', '.join(to_remove[:5])}). Wrong --from folder? "
                 "Use --allow-deletes if intended.")
    if args.check:
        print("Check passed; nothing written.")
        return

    write_export(posts, assets)
    if not (REPO / "themes" / "hyde" / "layouts").is_dir():
        sys.exit("themes/hyde is empty; run `git submodule update --init` first")
    run([args.hugo, "--cleanDestinationDir"])

    status = git_out("status", "--porcelain", "--", "content/posts")
    if not git_out("status", "--porcelain", "--", "content", "static", "docs").strip():
        print("No changes to publish.")
        return
    print("Post changes:\n" + (status or "  (none, only assets/theme output)\n"))
    if args.no_commit:
        print("Review with `git status` / `git diff`, then commit and push yourself.")
        return

    changed = [line[3:].rsplit("/", 1)[-1] for line in status.splitlines()]
    msg = "Publish: " + (", ".join(changed[:5]) + (" ..." if len(changed) > 5 else "")
                         if changed else "site rebuild")
    run(["git", "add", "-A", "--", "content/posts", "static/attachments", "docs"])
    run(["git", "commit", "-m", msg])
    if not args.no_push:
        branch = git_out("rev-parse", "--abbrev-ref", "HEAD").strip()
        run(["git", "push", "origin", branch])


if __name__ == "__main__":
    main()
