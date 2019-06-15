+++
title = "Install the latest tmux on Ubuntu 12.04"
date = "2013-12-06"
slug = "2013/12/06/install-the-latest-tmux-on-ubuntu-12.04"
Categories = ["Unix and Linux"]
+++

In this post, I will show you how to install the latest tmux on Ubuntu 12.04. First, we need to install 'add-apt-repository' command on our machine. This can be done by running these commands:

``` bash
sudo apt-get install software-properties-common

sudo apt-get install python-software-properties
```

After that you can add third party repository ( Ubuntu official repository does not have latest tmux at the moment )

``` bash
sudo add-apt-repository ppa:pi-rho/dev

sudo apt-get update 

sudo apt-get install tmux
```

I will suggest you to install the latest tmux if you want to use Tmuxinator.
