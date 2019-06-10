+++
date = "2009-08-31"
slug = "2009/08/31/melihat-pemakaian-hard-disk-di-linuxunix"
title = "Melihat pemakaian hard disk di Linux/Unix"
Categories = ["Unix and Linux"]
Tags = ["df", "du", "hard disk", "sun", "sun solaris", "unix", "Unix and Linux"]
+++

Jika kita menggunakan operating system Windows pasti dapat dengan mudahnya mencek pemakaian hard disk komputer kita melalui My Computer. Tapi bagaimana jika kita harus mengecek pemakaian hard disk ketika kita diharuskan memakai Linux Server atau Unix Server.

Untuk mengecek pemakaian hard disk di Linux/Unix kita dapat menggunakan beberapa perintah yaitu : ( gwa mengetesnya di server Sun Solaris )

``` bash
df
```

jika kita menggunakan perintah df maka akan keluar tampilan kira-kira seperti ini :

``` bash
/                  (/dev/dsk/c1t0d0s0 ): 2326264 blocks   444933 files
/devices           (/devices          ):       0 blocks        0 files
/system/contract   (ctfs              ):       0 blocks 2147483610 files
/proc              (proc              ):       0 blocks    29959 files
/etc/mnttab        (mnttab            ):       0 blocks        0 files
/etc/svc/volatile  (swap              ): 3997376 blocks   293539 files
/system/object     (objfs             ):       0 blocks 2147483464 files
/dev/fd            (fd                ):       0 blocks        0 files
/tmp               (swap              ): 3997376 blocks   293539 files
/var/run           (swap              ): 3997376 blocks   293539 files
/export/home       (/dev/dsk/c1t0d0s7 ):59435344 blocks  3683313 files
```

dari perintah tersebut dapat kita lihat pemakaian hard disknya, tetapi kalau cuma begitu saja agak sulit untuk membacanya. Oleh karena itu kita menggunakan tambahan option yaitu :

``` bash
df -h
```

dengan menjalankan perintah tersebut maka akan keluar tampilan seperti ini :

``` bash
Filesystem             size   used  avail capacity  Mounted on
/dev/dsk/c1t0d0s0      4.5G   3.4G   1.1G    77%    /
/devices                 0K     0K     0K     0%    /devices
ctfs                     0K     0K     0K     0%    /system/contract
proc                     0K     0K     0K     0%    /proc
mnttab                   0K     0K     0K     0%    /etc/mnttab
swap                   1.9G   968K   1.9G     1%    /etc/svc/volatile
objfs                    0K     0K     0K     0%    /system/object
fd                       0K     0K     0K     0%    /dev/fd
swap                   1.9G     0K   1.9G     0%    /tmp
swap                   1.9G    32K   1.9G     1%    /var/run
/dev/dsk/c1t0d0s7       28G    31M    28G     1%    /export/home
```

dari disitu sudah lebih terlihat berapa pemakaian hard disk dalam ukuran :

* K ( KiloByte )

* M ( MegaByte )

* G ( Gigabyte )

Namun perintah di atas cuma memperlihatkan ukuran dari directory utamanya saja ( tidak menampilkan detail pemakaian dari masing-masing folder ). Maka kita akan menggunakan perintah satu lagi untuk mengecek pemakaian dari masing-masing folder yaitu dengan menggunakan perintah :

``` bash
du -sh 
```

contoh pemakaiannya :

``` bash
du -sh /
3.7G
```

kalau untuk melist semua folder2nya cukup menambahkan tanda * di depannya menjadi seperti ini :

``` bash
du -sh /*
```

maka hasil yang akan dikeluarkan kira-kira seperti ini :

``` bash
26K   /TT_DB
   1K   /bin
   3K   /cdrom
   1K   /core
   2K   /core.svc.configd.1251605478.9
   2K   /core.svc.configd.1251606613.9
 347K   /dev
 134K   /devices
  49M   /etc
 2.2M   /export
   0K   /home
  14M   /instaler
  27M   /kernel
  24M   /lib
   8K   /lost+found
   1K   /mnt
  45M   /mysql-connector-odbc-5.1.4-solaris10-sparc-64bit
   0K   /net
  98M   /opt
  17M   /platform
 300M   /proc
 1.3M   /sbin
 3.6M   /system
  24K   /tmp
 2.9G   /usr
 295M   /var
   0K   /vol
```

Perintah-perintah diatas sangat berguna kalau misalnya kita harus mencari kenapa tiba-tiba pemakaian hard disk kita menjadi 99% ( yang kebanyakan disebabkan oleh folder logs yang tiba-tiba membesar ). Semoga berguna :)
