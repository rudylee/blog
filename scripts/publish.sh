#!/usr/bin/env bash
# Build the blog from the Obsidian vault (~/Documents/Rudy/blog) and publish it.
#
#   scripts/publish.sh preview   local preview at http://localhost:1313/blog/, drafts included
#   scripts/publish.sh build     build into docs/ only
#   scripts/publish.sh           build, commit docs/ and push master (goes live)
set -euo pipefail
cd "$(dirname "$0")/.."

VAULT_BLOG="$HOME/Documents/Rudy/blog"
[ -d "$VAULT_BLOG" ] || { echo "Can't find the vault's blog folder at $VAULT_BLOG" >&2; exit 1; }

# No --cleanDestinationDir: docs/ still holds pre-2019 title-based URLs that
# old links point at, and wiping it would break them.
build() { hugo; }

case "${1:-publish}" in
  preview) exec hugo server --buildDrafts --renderToMemory ;;  # never touches docs/
  build)   build ;;
  publish)
    branch=$(git branch --show-current)
    if [ "$branch" != master ]; then
      echo "On branch '$branch'. The live site is served from master; switch to it first." >&2
      exit 1
    fi
    build
    git add docs
    if git diff --cached --quiet; then
      echo "Nothing changed, nothing to publish."
      exit 0
    fi
    git commit -m "Publish blog $(date +%Y-%m-%d)"
    git push origin master
    echo "Pushed. GitHub Pages will update https://www.rudylee.com/blog/ in a minute or two."
    ;;
  *) echo "Usage: $0 [preview|build|publish]" >&2; exit 2 ;;
esac
