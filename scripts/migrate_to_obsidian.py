#!/usr/bin/env python3
"""One-off migration: Hugo posts -> Obsidian "Blog" folder.

Usage:
    python3 scripts/migrate_to_obsidian.py --out ~/path/to/Vault/Blog

What it does for each post in content/posts/*.md:
  * converts the TOML (+++) / YAML (---) front matter into Obsidian-friendly
    YAML properties: title, date, slug, categories, tags, publish
  * keeps `slug` exactly as-is -- it is the URL contract for the published site
  * copies every image the post references (/images/..., /wp-content/...,
    http://blog.rudylee.com/wp-content/...) into attachments/<post-name>/ and
    rewrites the links to relative paths (spaces in file names become "-")
  * leaves the body otherwise untouched

Requires Python 3.11+ (tomllib). No third-party packages.
"""
import argparse
import json
import re
import shutil
import sys
import tomllib
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS = REPO / "content" / "posts"
STATIC = REPO / "static"

# Markdown link target "](...)" or HTML src="..." pointing at a local asset.
ASSET_RE = re.compile(
    r'(?P<pre>\]\(|src=")'
    r'(?P<url>(?:https?://(?:blog|www)\.rudylee\.com)?/(?:images|wp-content)/[^)"]+)'
    r'(?P<post>\)|")'
)
BAD_FILENAME_CHARS = re.compile(r'[\\/:*?"<>|#^\[\]]')


def split_front_matter(text):
    m = re.match(r"\+\+\+\n(.*?)\n\+\+\+\n?", text, re.S)
    if m:
        return tomllib.loads(m.group(1)), text[m.end():]
    m = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    if m:
        return parse_simple_yaml(m.group(1)), text[m.end():]
    raise ValueError("no front matter found")


def parse_simple_yaml(block):
    """Enough YAML for the single `key: value` style post in this repo."""
    data = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        try:
            data[key.strip()] = json.loads(value)
        except json.JSONDecodeError:
            data[key.strip()] = value
    return data


def normalise_tag(tag):
    # Obsidian tags allow letters, digits, _ - / only. Hugo urlizes spaces to
    # "-", so "Ruby on Rails" -> "Ruby-on-Rails" keeps /tags/ruby-on-rails/.
    tag = tag.strip().strip("'\"")
    tag = re.sub(r"[^\w/-]+", "-", tag).strip("-")
    return tag


def yaml_value(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}[T\d:+-]*", value):
        return value  # unquoted so Obsidian treats it as a date
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)  # JSON string == valid YAML


def to_yaml(props):
    lines = ["---"]
    for key, value in props.items():
        if isinstance(value, list):
            if not value:
                continue
            lines.append(f"{key}:")
            lines.extend(f"  - {yaml_value(v)}" for v in value)
        else:
            lines.append(f"{key}: {yaml_value(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def note_filename(props):
    day = str(props["date"])[:10]
    title = BAD_FILENAME_CHARS.sub(" ", str(props["title"]))
    title = re.sub(r"\s+", " ", title).strip(" .'")
    return f"{day} {title}.md"


def migrate(out_dir: Path, force: bool):
    if out_dir.exists() and any(out_dir.iterdir()) and not force:
        sys.exit(f"{out_dir} is not empty; refusing to overwrite (use --force)")
    out_dir.mkdir(parents=True, exist_ok=True)

    seen_slugs, seen_names, problems = {}, set(), []
    count = 0
    for src in sorted(POSTS.glob("*.md")):
        meta, body = split_front_matter(src.read_text(encoding="utf-8"))
        meta = {k.lower(): v for k, v in meta.items()}
        stem = src.stem

        slug = meta.get("slug")
        if not slug:
            problems.append(f"{src.name}: missing slug")
            continue
        if slug in seen_slugs:
            problems.append(f"{src.name}: duplicate slug with {seen_slugs[slug]}")
        seen_slugs[slug] = src.name

        props = {
            "title": meta.pop("title"),
            "date": meta.pop("date"),
            "slug": meta.pop("slug"),
            "categories": list(meta.pop("categories", [])),
            "tags": list(dict.fromkeys(
                t for t in (normalise_tag(t) for t in meta.pop("tags", [])) if t)),
            "publish": True,
        }
        props.update(meta)  # keep anything unexpected rather than drop it

        attach_dir = out_dir / "attachments" / stem
        renamed = {}

        def replace(m):
            url = m.group("url")
            local = re.sub(r"^https?://[^/]+", "", url)
            source = STATIC / local.lstrip("/")
            if not source.is_file():
                problems.append(f"{src.name}: missing asset {url}")
                return m.group(0)
            name = re.sub(r"\s+", "-", source.name)
            if renamed.get(name, source) != source:
                problems.append(f"{src.name}: two assets named {name}")
            renamed[name] = source
            attach_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, attach_dir / name)
            return f'{m.group("pre")}attachments/{stem}/{name}{m.group("post")}'

        new_body = ASSET_RE.sub(replace, body)

        name = note_filename(props)
        if name in seen_names:
            name = name[:-3] + f" ({stem}).md"
        seen_names.add(name)
        (out_dir / name).write_text(to_yaml(props) + "\n" + new_body.lstrip("\n"),
                                    encoding="utf-8")
        count += 1

    # Verification: every relative attachment link must resolve.
    for note in out_dir.glob("*.md"):
        text = note.read_text(encoding="utf-8")
        for target in re.findall(r'(?:\]\(|src=")(attachments/[^)"]+)', text):
            if not (out_dir / target).is_file():
                problems.append(f"{note.name}: broken link {target}")
        if ASSET_RE.search(text):
            problems.append(f"{note.name}: unconverted asset link left")

    print(f"Migrated {count} posts into {out_dir}")
    print(f"Attachments: {sum(1 for p in (out_dir / 'attachments').rglob('*') if p.is_file())} files")
    if problems:
        print("\nProblems:")
        print("\n".join(f"  - {p}" for p in problems))
        sys.exit(1)
    print("All slugs unique, all attachment links resolve.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, type=Path,
                    help="target folder, e.g. ~/Vault/Blog")
    ap.add_argument("--force", action="store_true",
                    help="write into a non-empty folder")
    args = ap.parse_args()
    migrate(args.out.expanduser().resolve(), args.force)
