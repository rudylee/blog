+++
title = "Symbolic Links With Vagrant Windows"
date = "2014-10-27"
slug = "2014/10/27/symbolic-links-with-vagrant-windows"
Categories = ["Unix and Linux", "Vagrant"]
+++

There are few known limitations when using Vagrant on Windows machine. One of these limitations is the lack of symbolic links support on synced folder. 

Symbolic links are used heavily by NPM to create shortcut for the libraries. I posted more details about this here: [http://blog.rudylee.com/2013/10/24/fix-npm-symlink-problem-in-vagrant/](http://blog.rudylee.com/2013/10/24/fix-npm-symlink-problem-in-vagrant/)

Most of the time, you can get away with 'npm --no-bin-link' solution. However, you need more robust solution if you are using complex tools such as Grunt or Yeoman. 

In this post, I'll show you the proper way to add symbolic links support to your Vagrant machine.

First, you need to add this code snippet inside your Vagrantfile

``` bash
config.vm.provider "virtualbox" do |v|
    v.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
end
```

VirtualBox disables symbolic links for security reasons. In order to pass this restriction, you need to boot up the Vagrant machine in Administrator mode.

You can do this by simply right clicking on your Command Prompt or Git Bash icon and click 'Run as Administrator'. See the picture below if you can't find it.

[![](/images/run_as_admin.png)](/images/run_as_admin.png)

After that, boot up the Vagrant machine normally with 'vagrant up' command. Wait until the machine boots up, SSH to the machine and try to create symbolic link in the synced folder.

## File path 255 character limit 

Another annoying problem you might encounter is file path character limit. This happens quite often if you are using a node module with long name. You can easily solve this by following these steps:

### Create 'node_modules' folder in your home folder

``` bash
  mkdir ~/node_modules
```

### Add symbolic link to the 'node_modules' folder you just created inside your project folder

``` bash
  ln -sf ~/node_modules /vagrant/your-project-folder
```

This solution will ensure that all the node modules are stored inside home directory instead of synced folder.
