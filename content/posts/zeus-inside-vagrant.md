+++
title = "Zeus inside Vagrant"
date = "2013-09-13"
slug = "2013/09/13/zeus-inside-vagrant"
Categories = ["Ruby on Rails"]
+++

I have been using Vagrant as my development environment for the last couple weeks. It has been very helpful as I prefer to use Linux as my development environment and I can only use Windows at my workplace. With Vagrant, I can easily set up new Linux machine, install Vim plus all the plugins and completely separate development machine for each project. 

Today, I was trying to use Zeus to speed up my Rspec test inside one of the Rails projects. I found this gem through a screencast by Ryan Bates about Fast Test. 

Install Zeus is pretty easy, you just need to run this command on your terminal:

``` bash 
gem install zeus
```

After that you just need to go to the directory of your Rails app and start the Zeus server using this command:

``` bash
zeus start
```

However, when I got an error when I was trying to ran that command. Here is the error:

``` bash
vagrant@precise32:/vagrant$ zeus start
Starting Zeus server
[ready] [crashed] [running] [connecting] [waiting]
boot
└── default_bundle
    ├── development_environment
    │   └── prerake
    └── test_environment
        ├── cucumber_environment
        └── test_helper

Available Commands: [waiting] [crashed] [ready]
zeus rake
zeus runner (alias: r)
zeus console (alias: c)
zeus server (alias: s)
zeus generate (alias: g)
zeus destroy (alias: d)
zeus dbconsole
zeus cucumber
zeus test (alias: rspec, testrb)
It looks like Zeus is already running. If not, remove .zeus.sock and try again.
```

You can see on the last line that it's complaining something about .zeus.sock. The solution is pretty easy, you just need to add environment variable to your Vagrant machine. Use this command to add environment variable:

``` bash
export ZEUSSOCK=/tmp/zeus.sock
```

Also make sure you use the latest version of Zeus. Add this line inside your Gemfile:

``` ruby
# Use Zeus
gem 'zeus', ">= 0.13.4.pre2"
```

Run 'bundle' to install the gem and update the version. You should be able to run 'zeus start' now and other Rails commands.
