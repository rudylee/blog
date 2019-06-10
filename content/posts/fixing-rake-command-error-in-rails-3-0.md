+++
date = "2011-05-29"
slug = "2011/05/29/fixing-rake-command-error-in-rails-3-0"
title = "Fixing rake command error in rails 3.0.7"
Categories = ["Ruby on Rails"]
Tags = ["application folder", "laptop", "little bit", "pop up window", "rails", "rake", "rudy"]
+++

Today I was trying to add rails project to Netbeans 6.9,but suddenly there is a pop up window that said "Rake task fecthing failed" with bunch of other errors. After that, I tried go to my application folder and try to run the rake command 

    
``` ruby    
rake -D
```
    
However I got this error
    
``` bash
rudy@rudy-laptop:~/www/depot$ rake -D
rake aborted!
undefined method `task' for #<depot::application:0x91fa9c4>

(See full trace by running task with --trace)
```
    
After a little bit research, I found that I have to uninstall my rake 0.9 and install 0.8.7 instead. So I ran this command :

``` bash
gem uninstall rake -v 0.9
gem install rake -v 0.8.7
```
    
Edited the gem file and added this code inside that file :

``` ruby
gem 'rake', '0.8.7'
```

Last step is update the bundle
    
``` bash    
bundle update
```

After that you can try run your rake command or import your project to Netbans, it's should be fine.

UPDATE :
It turns out that the problem is because I was using rake 0.9 and it's break out all the installation.

``` bash
gem install bundler
```

You might want to install bundler if you encounter some errors related to Netbeans couldn't find bundler setup. Another thing is you have to add gem path to your Netbeans ( Tools > Rubygems ) and add your gem path. 

I am using rvm to install ruby and also rails. So I run this command to find gem path

``` bash
rvm gemdir
```
    



