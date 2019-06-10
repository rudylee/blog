+++
date = "2010-07-20"
slug = "2010/07/20/installing-openvz-and-webvz-in-centos-5-5"
title = "Installing OpenVZ and WebVZ in Centos 5.5"
Categories = ["Unix and Linux"]
Tags = ["centos", "containers", "grub", "instances", "kernels", "linux kernel", "management gui", "openvz", "operating system", "physical server", "repo", "repos", "repository", "Ruby on Rails", "virtual environments", "virtual private servers", "web application", "wiki", "xen", "yum"]
+++

> OpenVZ is an operating system-level virtualization technology based on the Linux kernel and operating system. OpenVZ allows a physical server to run multiple isolated operating system instances, known as containers, Virtual Private Servers (VPSs), or Virtual Environments (VEs).


Now we'll try to install OpenVZ in Centos. OpenVS is an operating system-level VPS so you need to install Host Operating System ( if you are using hardware virtualization like Xen or VMware then you don't have to install an Operating System ).

The first step is that you must install the Centos ( I am using Centos 5.5 ). I won't explain about how to install it so you must find the tutorial yourself :P

Let's say you already installed the Centos, next step is updating your yum package manager. Here are the steps :
	
  * Download the OpenVZ repo from http://download.openvz.org/openvz.repo
	
  * Put it in /etc/yum.repos.d directory
	
  * Run the yum update command

Wait until the process is complete, it will downloading all the necessary update package. ( you can find the complete tutorial in [OpenVZ Wiki](http://wiki.openvz.org/Yum) ).

Now we will install the OpenVZ, type this to install the OpenVZ :

    
``` bash
  yum install ovzkernel vzctl
```


If the installation running smooth you will have OpenVZ installed, reboot your machine :

``` bash
  reboot
```

Press any key when the Grub screen is popping out. If it's installed then you must have 3 kernels. Choose the top kernel ( it's the OpenVZ kernel, in my machine the name is CentOS ( 2.6.18-194.3.1.el5.028stab069.6 ).

Log in to your machine as usual, now you are running on OpenVZ kernel. The next step is we will install WebVZ ( the OpenVZ management GUI ). The WebVZ, like it's name, is a web application that runs on Ruby on Rails. So you must have Ruby on Rails in your machine to use the WebVZ.

To help us installing the Ruby on Rails we will use [Ruby Works ](http://rubyworks.rubyforge.org/). Ruby Works is one of the CentOS repository that provides with the newest installer of Ruby, Gem and Rails.

Here are the steps :

1.Download the repo file

``` bash
wget http://rubyworks.rubyforge.org/RubyWorks.repo
```

2.Put it the file in the /etc/yum.repos.d

3.yum update
    
``` bash
  yum update
```

4.Installing the ruby packages

``` bash    
  yum install ruby ruby-devel ruby-irb ruby-rdoc ruby-ri
```

5.Check the installed Ruby using this command ( it should print out the ruby version eg: ruby 1.8.6 )

    
``` bash
  ruby -v
```

6.Then download the latest gem at [Rubyforge](http://rubyforge.org/frs/?group_id=126)

7.After download the latest gem, extract it, go the folder and run the installer

``` bash
  ruby setup.rb
```

8.Check if the gem is installed successfully ( it should return the version too )
    
``` bash
  gem -v
```

9.Run the gem update to make sure the gem is up to date.

``` bash    
  gem update
```

10.Install the rails

``` bash
  gem install rails -v=2.3.2
```

11.The WebVZ need sqlite to run, so you must install the sqlite and the gcc compiler
    
``` bash
  yum install sqlite-devel
  yum install gcc make
```

12.And the last is installing the sqlite for ruby
    
``` bash
  gem install sqlite3-ruby -v=1.2.5
```

13.Download the [WebVZ installer](http://webvz.sourceforge.net/download.html) from it's website. Extract it and run the application.
    
``` bash
  cd webvz
  ruby script/server
```

That's all, then you can access it via web browser http://your-ip:3000. the username is admin and the password is admin123.

Update : ( run the WebVZ as daemon )
to run WebVZ as daemon just go to it's directory run this command instead of plain "ruby script/server"

``` bash
  ruby script/server &>/dev/null &
```

and to make it's run everytime you boot the machine ( put it in rc.local )
    
``` bash
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

cd /usr/local/webvz/ && /usr/bin/ruby script/server &>/dev/null &

exit 0
```
