+++
date = "2009-07-18"
slug = "2009/07/18/setting-mod_rewrite-atau-sef-joomla-di-nginx"
title = "Setting mod_rewrite atau SEF Joomla di Nginx"
Categories = ["Unix and Linux"]
Tags = ["freebsd", "mod_rewrite", "nginx", "PHP"]
+++

Yap sambil menunggu server World of Warcraft yang tak kunjung up-up gwa buat tutorial sedikit tentang setting mod_rewrite Joomla di Nginx. Sudah pada tau Nginx ? kalau belum tau gwa kasih tau dah. Nginx itu adalah salah satu web server seperti Apache, Lighttpd, Apache Tomcat, Jetty, IIS, Zeus dan lainnya. Nginx ini ( dibacanya Engine X ) kabarnya sih lebih cepat dan stabil dibandingkan Apache yang sudah tersohor sebagai server PHP. Untuk detail lengkap tentang fitur-fiturnya silakan baca [link ini.](http://en.wikipedia.org/wiki/Nginx)

Kalau pengen liat perbandingan kecepatannya dapat googling sendiri soalnya gwa juga blom coba ngetes kecepatannya soalnya gwa cuma pengen ngetes aja bedanya makai Nginx dan Lighttpd. Setelah gwa menggunakan kedua web server yang katanya lebih "cepat" dari Apache tersebut gwa menemukan salah satu fitur penting yang kurang yaitu kemampuan kedua web server tersebut untuk membaca file .htaccess, dan itu artinya apa ? itu artinya kita tidak bisa langsung memakai fitur-fitur mod_rewrite yang sudah disediakan engine-engine dan framework-framework seperti CakePHP, Joomla, dan Wordpress.

Tapi untunglah teknologi sudah maju, cukup search-search dikit ternyata langsung dapat deh tutorial mod_rewrite Joomla di Nginx. Tapi walaupun teknologi sudah maju tapi ternyata tutorial yang didapat tidak cukup maju ( alias dicoba-coba ga jalan ). Jadi daripada ntar ada orang yang bernasib sama kek gwa makanya dengan senang hati gwa bikin ini tutorial hohoho. Ya udah kita back to topic tar kelamaan out of topic.

Nah, jadi untuk membuat mod_rewrite atau fitur SEF Joomla jalan di Nginx kita hanya perlu membuat rulesnya dan dengan sedikit tricky way kita bisa buat semua berjalan seperti di Apache. Kira-kira begini settingan nginx.conf gwa ( gwa ga bakal jelasin cara nginstall Nginx dan setting PHP ) :


    
    
    #user  nobody;
    worker_processes  1;
    
    #error_log  logs/error.log;
    #error_log  logs/error.log  notice;
    #error_log  logs/error.log  info;
    
    #pid        logs/nginx.pid;
    
    
    events {
        worker_connections  1024;
    }
    
    http {
        include       mime.types;
        default_type  application/octet-stream;
    
        #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
        #                  '$status $body_bytes_sent "$http_referer" '
        #                  '"$http_user_agent" "$http_x_forwarded_for"';
    
        #access_log  logs/access.log  main;
    
        sendfile        on;
        #tcp_nopush     on;
    
        #keepalive_timeout  0;
        keepalive_timeout  65;
    
        #gzip  on;
    
        server {
            listen       80;
            server_name  binus-access.com v2.binus-access.com;
    
            #charset koi8-r;
    
            #access_log  logs/host.access.log  main;
    	location / {
    		root   /usr/local/www/data;
    		index  index.html index.htm index.php;
    		error_page 404 = @joomla; 
    	}
    
    	location @joomla { 
    		rewrite ^(.*)$ /index.php?q=$1 last;
    	}
    
            #error_page  404              /404.html;
    
            # redirect server error pages to the static page /50x.html
            #
            error_page   500 502 503 504  /50x.html;
            location = /50x.html {
                root   /usr/local/www/nginx-dist;
            }
    
            # proxy the PHP scripts to Apache listening on 127.0.0.1:80
            
            location ~ \.php$ {
    		fastcgi_pass 127.0.0.1:9000;
    		fastcgi_index index.php;
    		fastcgi_param SCRIPT_FILENAME /usr/local/www/data$fastcgi_script_name;
    		include fastcgi_params;	
            }
    
            # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
            
    #	location ~ \.php$ {
    #            root           html;
    #            fastcgi_pass   127.0.0.1:9000;
    #            fastcgi_index  index.php;
    #            fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #            include        fastcgi_params;
    #        }
    
             #deny access to .htaccess files, if Apache's document root
             #concurs with nginx's one
            
       #     location ~ /\.ht {
       #         deny  all;
       #   }
        }
    
        # another virtual host using mix of IP-, name-, and port-based configuration
        #
        #server {
        #    listen       8000;
        #    listen       somename:8080;
        #    server_name  somename  alias  another.alias;
    
        #    location / {
        #        root   html;
        #        index  index.html index.htm;
        #    }
        #}
    
    
        # HTTPS server
        #
        #server {
        #    listen       443;
        #    server_name  localhost;
    
        #    ssl                  on;
        #    ssl_certificate      cert.pem;
        #    ssl_certificate_key  cert.key;
    
        #    ssl_session_timeout  5m;
    
        #    ssl_protocols  SSLv2 SSLv3 TLSv1;
        #    ssl_ciphers  ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;
        #    ssl_prefer_server_ciphers   on;
    
        #    location / {
        #        root   html;
        #        index  index.html index.htm;
        #    }
        #}
    
    }
    
    
    
    
    Jadi kalau dilihat-lihat dari settingan nginx.conf gwa, cuma ada 2 hal bagian yang harus diperhatikan yaitu bagian ini :
    
    
    
    	location / {
    		root   /usr/local/www/data;
    		index  index.html index.htm index.php;
    		error_page 404 = @joomla; 
    	}
    
    	location @joomla { 
    		rewrite ^(.*)$ /index.php?q=$1 last;
    	}
    



Kalau ditranslate kira-kira bacanya begini : jika ada error page 404 maka dia akan set rules menjadi @joomla. Semoga tutorial ini berguna, kalau ga jalan coba dilihat-lihat dolo settingannya lagi soalnya TESTED dan WORKS ( silakan ke [www.binus-access.com](http://www.binus-access.com) ) itu adalah web yang pakai Nginx. Btw, selain itu ada beberapa web besar yang menggunakan Nginx juga yaitu Kaskus dan Wordpress. Jadi itu juga menambah keyakinan gwa untuk menggunakan Nginx ini. Sekian tutorial dari gwa, kalau ada pertanyaan comment ato add YM aja di channel_life.



