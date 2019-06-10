+++
title = "Reopen Last Commit in Git"
date = "2016-01-20"
slug = "2016/01/20/reopen-last-commit-in-git"
Categories = ["Git"]
Tags = ["git"]
+++

Run the command below if you want to reopen the last commit in your git

```bash
git reset --soft HEAD~
```

This is useful if you miss something in your last commit. Instead of creating new commit and squashing it, you can open last commit and fix it there.
