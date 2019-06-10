+++
title = "Fix npm symlink problem in Vagrant"
date = "2013-10-24"
slug = "2013/10/24/fix-npm-symlink-problem-in-vagrant"
Categories = ["Unix and Linux"]
+++

Today I encountered weird symlink error when trying to install npm modules on my Vagrant Ubuntu Box. The error says "pm ERR! Error: UNKNOWN, symlink '../which/bin/which'". 

After quick Google, it turns out the problem is caused by npm trying to create symlink which is not supported on Windows ( I am using Windows 8 as my host machine ). 

Here is quick solution which allow you to install npm modules without creating any symlinks :

``` bash
npm install --no-bin-link
```
