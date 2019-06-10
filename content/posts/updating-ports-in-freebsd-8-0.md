+++
date = "2010-06-28"
slug = "2010/06/28/updating-ports-in-freebsd-8-0"
title = "Updating ports in FreeBSD 8.0"
Categories = ["Unix and Linux"]
Tags = ["application folder", "freebsd", "mirror", "ports", "repository", "several ways", "share examples", "Ubuntu"]
+++

Ports is the applications repository in FreeBSD. Unlike Ubuntu that provides you with command "apt-get", in FreeBSD you must manually go to the application folder in "/usr/ports" ( the folder where Ports remain ) and search for the application that you want to install. But what's the differences between you compile it yourself and using ports. The answer is "dependencies".

Enough with the introduction, let's go the main topic. So we are going to update the Ports using cvsup. Yeah... yeah... I know that there are several ways to update the ports, but I prefer to use cvsup ( because it's the way I taught ). The steps are :

1.Install the cvsup

``` bash
  pkg_add -vr cvsup-without-gui
```

2.Copy the ports-supfile from example

``` bash
  cp /usr/share/examples/cvsup/ports-supfile .
```

3.Rehash
    
``` bash
  rehash
```

4.Edit the ports-supfile, find the line that say CHANGETHIS.FreeBSD.org. Change it with the mirror that is near you ( I am using BizNet )

5.Run the ports-supfile using cvsup

``` bash
  cvsup -g -L 2 ports-supfile
```

Wait until the process is complete and your ports will be updated.
