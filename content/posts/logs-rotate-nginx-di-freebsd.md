+++
date = "2010-01-13"
slug = "2010/01/13/logs-rotate-nginx-di-freebsd"
title = "Logs Rotate Nginx di FreeBSD"
Categories = ["Unix and Linux"]
Tags = ["freebsd", "log rotate", "logs", "nginx", "rotate logs"]
+++

File logs sering kali menjadi sebuah masalah ketika ukurannya menjadi semakin besar dan memakan sebagian besar hard disk server kita, tetapi di sisi lain file logs juga berguna untuk mencari masalah yang terjadi di server kita.

Gwa juga sempat mengalami beberapa masalah dengan file logs nginx di server FreeBSD. Permasalahan bermula dikarenakan gwa salah mengeset ukuran dari folder '/var/logs' yang hanya berukuran 2 Gb saja ( padahal file logs ukurannya bisa sampai 10 Gb keatas ). Hal tersebut tentu saja mengakibatkan banyak user-user binus-access yang "bernyanyi" karena ga bisa login.

Selain itu ukuran file logs yang semakin lama semakin besar dan terkonsentrasi dalam 1 file tentu saja sangat mempersulit kita dalam melakukan tracing jika terjadi sesuatu, entah itu kena hack, kena dos, kena flood, kompor meleduk, anak hilang, blum sarapan, dll. Oleh karena itu kita akan menggunakan salah satu solusi yaitu rotate file log sehingga file log itu akan dipecah2 menjadi file2 kecil setiap harinya. 

Kalau biasanya file logs itu cuma bentuknya "error.log" nanti akan muncul banyak file log sesuai dengan hasil rotate kita, contohnya "error.log.0.bz1" atau "error.log.1.bz2".

Jadi langkah pertama yang gwa lakukan adalah mengubah tempat penyimpanan file log ke '/usr/local', kira2 begini lah settingannya di nginx.conf

``` apache
access_log /usr/local/log/binus-access.com.access.log;
error_log /usr/local/log/binus-access.com.error.log;
```
    
setelah itu kita cuma perlu melakukan perubahan di newsyslog.conf supaya bisa merotate log kita, kira-kira begini isi newsyslog.conf ( /etc/newsyslog.conf )

``` bash    
/var/log/all.log                        600  7     *    @T00  J
/var/log/amd.log                        644  7     100  *     J
/var/log/auth.log                       600  7     100  *     JC
/var/log/console.log                    600  5     100  *     J
/var/log/cron                           600  3     100  *     JC
/var/log/daily.log                      640  7     *    @T00  JN
/var/log/debug.log                      600  7     100  *     JC
/var/log/kerberos.log                   600  7     100  *     J
/var/log/lpd-errs                       644  7     100  *     JC
/var/log/maillog                        640  7     *    @T00  JC
/var/log/messages                       644  5     100  *     JC
/var/log/monthly.log                    640  12    *    $M1D0 JN
/var/log/pflog                          600  3     100  *     JB    /var/run/pflogd.pid
/var/log/ppp.log        root:network    640  3     100  *     JC
/var/log/security                       600  10    100  *     JC
/var/log/sendmail.st                    640  10    *    168   B
/var/log/slip.log       root:network    640  3     100  *     JC
/var/log/weekly.log                     640  5     1    $W6D0 JN
/var/log/wtmp                           644  3     *    @01T05 B
/var/log/xferlog                        600  7     100  *     JC
/usr/local/log/*.log    root:wheel      640  7     *    @T00  GJ    /var/run/nginx.pid
```

jadi sebenarnya yang harus kita tambahkan adalah line terakhir yaitu
    
``` bash
/usr/local/log/*.log    root:wheel      640  7     *    @T00  GJ    /var/run/nginx.pid
```
    
/usr/local/log/*.log adalah tempat penyimpanan file log kita. Sementara untuk root:wheel itu adalah nama usernya, sementara sisanya ikutin saja la soalnya saya juga ga ngerti hohohoho.

Nah setelah setting itu, kita tinggal menunggu satu hari maka secara otomatis logs file kita akan ter-rotate sendiri. Silakan dicoba sendiri :D
