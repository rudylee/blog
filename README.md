# Blog

My personal blog, https://www.rudylee.com/blog/. Built with
[Hugo](https://gohugo.io/) and the [hyde-hyde](https://github.com/htr3n/hyde-hyde)
theme, published from `docs/` on the `master` branch by GitHub Pages.

Posts are written in Obsidian, not in this repo. Hugo reads them straight from
the vault's `blog/` folder (`~/Documents/Rudy/blog`, set in `config.toml` under
`[module]`).

# Write a post

1. In Obsidian, add a note to `blog/` named `YYYY-MM-DD Title.md` with these properties:

   ```yaml
   ---
   title: "My post title"
   date: 2026-11-21
   slug: "2026/11/21/my-post-title"
   categories:
     - "Programming"
   tags:
     - Hugo
   draft: true
   ---
   ```

   `slug` is the post's URL (`/blog/<slug>/`). Never change it on a published
   post, or old links break.

2. Paste images into `blog/attachments/<post-name>/` and link them as
   `![](attachments/<post-name>/image.png)`. They show in Obsidian and on the site.

3. When it's ready, set `draft: false` (or delete the line). Drafts only show in preview.

# Preview and publish

```
scripts/publish.sh preview   # http://localhost:1313/blog/, drafts included, docs/ untouched
scripts/publish.sh build     # build into docs/ only
scripts/publish.sh           # build, commit docs/ and push master: goes live
```

Publishing only works on `master`. `docs/` is never wiped, because it still
holds pre-2019 URLs that old links point at.

# History

`scripts/migrate_to_obsidian.py` was the one-off script that moved the old
`content/posts/` into the vault in November 2026. The posts are in git history
if ever needed.
