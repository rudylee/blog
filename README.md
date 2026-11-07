# Blog

My personal blog. Built with [Hugo](https://gohugo.io/) and [hyde-hyde](https://github.com/htr3n/hyde-hyde) template.

# Add new blog post

```
hugo new posts/blog-title.md
```

# Run the server

```
hugo server -D
```

# Migrate posts to Obsidian

One-off script that copies every post into an Obsidian folder (YAML
properties, images in `attachments/<post>/`, relative links). The `slug`
property is kept as-is and is what decides the published URL.

```
python3 scripts/migrate_to_obsidian.py --out ~/path/to/Vault/Blog
```

Needs Python 3.11+. It refuses to write into a non-empty folder unless
`--force` is given, and exits non-zero if any slug or image link is broken.
