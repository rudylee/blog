+++
date = "2011-04-13"
slug = "2011/04/13/apache-geoip"
title = "Apache GeoIP"
Categories = ["Unix and Linux"]
Tags = ["apache module", "australia", "country code", "geoip", "htaccess file", "ip", "restart apache", "rewriterule", "www canada"]
+++

Apache GeoIP is an apache module for detecting your visitor's IP and block/redirect them to another website. Installing and configuring GeoIP is very easy in Ubuntu. Here are the steps :

1.Install the Apache GeoIP module and restart apache webserver

``` bash    
sudo apt-get install libapache2-geoip
sudo /etc/init.d/apache2 restart
```

2.Create the .htaccess file and put in your webroot folder / website folder
    
``` apache
GeoIPEnable On

# Redirect one country
RewriteEngine on
RewriteCond %{ENV:GEOIP_COUNTRY_CODE} ^AU$
RewriteRule ^(.*)$ http://www.canada.com$1 [L]
```


In the example above, GeoIP will check whether the visitor is from Australia or not. If the visitor is from Australia then apache will redirect the visitor to http://www.canada.com. Quite simple and straight forward. You can see another example in here[ http://www.maxmind.com/app/mod_geoip](http://www.maxmind.com/app/mod_geoip) ( ignore the GeoIPDBFile because it will cause error ).
