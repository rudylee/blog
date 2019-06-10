+++
date = "2010-01-27"
slug = "2010/01/27/install-php-fpm-di-freebsd-dengan-web-server-nginx"
title = "Install PHP-FPM di FreeBSD dengan web server Nginx"
Categories = ["Unix and Linux"]
Tags = ["freebsd", "PHP"]
+++

Setelah mengalami beberapa problem dengan web server [Binus Access](http://www.binus-access.com) yang menggunakan Nginx, akhirnya gwa memutuskan untuk mengganti php-cgi menjadi php-fpm.

Untuk mengubah php-cgi menjadi php-fpm ternyata tidak lah sulit, apalagi dengan adanya fitur ports dari FreeBSD. Pertama-tama cukup download file ports php-fpm dari websitenya [php-fpm ](http://php-fpm.org/download/).

Untuk versi nya sendiri bisa disesuaikan dengan versi php anda, kalau gwa sih menggunakan versi php 5.2.10. Jadi hal pertama yang gwa lakukan adalah mendownload php-fpm versi [5.2.10](http://php-fpm.org/downloads/freebsd-port/).

Setelah itu tinggal extract aja file php-5.2.10-fpm-0.5.13.tar.gz kemudian pindahin folder php5-fpm nya ke folder /usr/ports/lang. Kemudian tinggal jalankan perintah make dan make install.

Tunggu proses instalasi selesai kemudian ubah file /etc/rc.conf dan tambahkan 

``` apache    
    php_fpm_enable=”YES”
```

masuk ke dalam settingan nginx.conf di /usr/local/etc/nginx/nginx.conf dan ubah beberapa settingan di

``` apache
location / {
    root /usr/local/www/nginx;
    index index.php index.html index.htm;
}

location ~ \.php$ {
    fastcgi_pass 127.0.0.1:9000;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME /usr/local/www/nginx$fastcgi_script_name;
    include fastcgi_params;
}
```
    
fastcgi_param SCRIPT_FILENAME /usr/local/www/nginx$fastcgi_script_name; ini adalah tempat folder root web anda berada.

Lalu lanjut dengan edit file php-fpm.conf di /usr/local/etc/php-fpm.conf
    
``` apache
    nobody</value> –>
    nobody</value> –>
```

ubah nobody menjadi www
    
``` xml
    <value name="”user”">www</value>
    <value name="”group”">www</value>
``` 
    
matikan service sebelumnya yaitu php-cgi dan jalankan php-fpm nya

``` bash
    /usr/local/etc/rc.d/php-fpm start
```
    
kemudian tinggal testing saja apakah berjalan lancar atau tidak settingannya. Moga-moga lebih stabil dan ga down lagi hohohoho :D
