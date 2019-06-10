+++
title = "Trailing Characters ^M"
date = "2013-09-18"
slug = "2013/09/18/trailing-characters-m"
Categories = ["Unix and Linux"]
+++

This morning I ran into weird errors in one of my Vagrant machine. These errors come up when I was trying to run tmux and vim:

``` bash
Error detected while processing /home/vagrant/.vimrc:
line    1:
E488: Trailing characters: nocompatible^M
line    2:
E488: Trailing characters: nu^M
line    3:
E488: Trailing characters: nobackup^M
line    4:
E488: Trailing characters: nowritebackup^M
line    5:
E488: Trailing characters: noswapfile^M
line    6:
E488: Trailing characters: hlsearch^M
line    7:
E488: Trailing characters: ruler^M
line    8:
E474: Invalid argument: laststatus=2^M
line    9:
E474: Invalid argument: tabstop=2^M
line   10:
E474: Invalid argument: shiftwidth=2^M
line   11:
E488: Trailing characters: expandtab^M
Vim: Error reading input, exiting...ne down, b/u/k: up, q: quit
Vim: Finished.
Press ENTER or type command to continueVim: Error reading input, exiting...
Vim: Finished.
```

I had similar problem before when trying to edit file from Windows machine inside vim. ^M character is added by Windows machine to mark newline in their files. 

The quickest solution to fix this is by installing 'dos2unix' software and let it fix the file for you. In Ubuntu, you can run this command to install it:

``` bash
sudo apt-get install dos2unix
```

And fix the file by typing this:

``` bash
dos2unix <file>
```

It will automatically remove all the trailing characters for you.
