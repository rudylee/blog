+++
title = "Enable HTTP authentication on certain domain"
date = "2014-09-18"
slug = "2014/09/18/enable-http-authentication-on-certain-domain"
Categories = ["Unix and Linux"]
+++

Basic HTTP authentication is one simple way to limit public access to your website prior to launch. 

The first thing you need is .htaccess file which contains all the configurations. The second one is .htpasswd containing username and password. You can use this website to generate .htpasswd file for you [http://www.htaccesstools.com/htpasswd-generator/](http://www.htaccesstools.com/htpasswd-generator/)

In the sample below, I am trying to enable HTTP authentication only on certain domain. On the first line, I set enviroment variable if the domain name is equal to "www.bundabergfestival.com.au". On line 7, I tell .htaccess file to deny any access by using the live_uri variable. I hope that explanation is pretty straight forward.

``` bash
SetEnvIf Host "^www.bundabergfestival.com.au" live_uri
AuthName "Bundaberg Festival Website Coming Soon"
AuthType Basic
AuthUserFile /var/app/.htpasswd
AuthGroupFile /dev/null
require valid-user
Order allow,deny
Allow from all
Deny from env=live_uri
Satisfy any
```
