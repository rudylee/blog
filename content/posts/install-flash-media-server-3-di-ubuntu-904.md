+++
date = "2009-09-01"
slug = "2009/09/01/install-flash-media-server-3-di-ubuntu-904"
title = "Install Flash Media Server 3 di Ubuntu 9.04"
Categories = ["Unix and Linux"]
Tags = ["coding", "flash media server", "fms", "Ubuntu", "Unix and Linux"]
+++

Hari ini gwa mencoba menginstall ulang Flash Media Server 3 untuk TV Streaming ( Bee Watch ) pada Ubuntu 9.04. Jadi proses install dimulai dari install Ubuntu 9.04 yang memakan waktu 1 hari dikarenakan hard disk yang rusak ( untung udah ganti dengan yang baru ).

Nah jadi setelah setting-setting sana sini mulailah install FMS ( Flash Media Server ), dimulai dari copy installer FMS 3 ke server trus mulai deh extract dengan menggunakan perintah

``` bash
tar zxvf 
```

setelah selesai extract dilanjutkan dengan menginstall flash media servernya, masuk ke folder FMS nya dan ketik command berikut

``` bash
./installFMS
```

ikuti langkah-langkahnya, isi serial number, set port, dan settingan-settingan lainnya. Ketika proses install selesai seharusnya akan muncul error message yang mengatakan NSPR library tidak tersedia, kira-kira begini error messagenya :

``` bash
Starting Adobe Flash Media Server (please check /var/log/messages)
Error: Flash Media Server needs the NSPR library installed.
Admin server:fmsadmin command:start
Starting Adobe Flash Media Admin Server (please check /var/log/messages)
``` 

Hal itu disebabkan karena FMS membutuhkan 2 library yaitu libnspr4.so dan libasneu.so.1. Untuk libnspr4.so kita tinggal melakukan apt-get saja.

``` bash
apt-get install libnspr4-dev
```

sementara untuk libasneu.so.1 sudah disediakan oleh FMS dan kita tinggal mengarahkannya. Pertama-tama buat file adobe_fms.conf di folder /etc/ld.so.conf.d kemudian file tersebut isi dengan path ke folder FMS

``` bash
cd /etc/ld.so.conf.d
vim adobe_fms.conf
```

isi dengan /opt/adobe/fms
untuk menjalankan konfigurasinya jalankan perintah ldconfig

``` bash
ldconfig
```

dan

``` bash
ldd /opt/adobe/fms/fmscore
```

untuk mengecek hasil konfigurasi
jika benar maka akan muncul tampilan seperti ini :

``` bash
linux-gate.so.1 =>  (0xb80af000)
libpthread.so.0 => /lib/tls/i686/cmov/libpthread.so.0 (0xb8090000)
libnspr4.so => /usr/lib/libnspr4.so (0xb805a000)
libplc4.so => /usr/lib/libplc4.so (0xb8054000)
libplds4.so => /usr/lib/libplds4.so (0xb8050000)
libasneu.so.1 => /opt/adobe/fms/libasneu.so.1 (0xb8047000)
librt.so.1 => /lib/tls/i686/cmov/librt.so.1 (0xb803e000)
libdl.so.2 => /lib/tls/i686/cmov/libdl.so.2 (0xb803a000)
libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0xb7f4b000)
libm.so.6 => /lib/tls/i686/cmov/libm.so.6 (0xb7f24000)
libgcc_s.so.1 => /lib/libgcc_s.so.1 (0xb7f15000)
libc.so.6 => /lib/tls/i686/cmov/libc.so.6 (0xb7db2000)
/lib/ld-linux.so.2 (0xb80b0000)
```

setelah itu coba jalankan FMS nya sekarang

``` bash
/etc/init.d/fms start
```

jika terjadi error / tidak jalan maka anda harus menjalankan perintah-perintah lagi dibawah ini

``` bash
cd /usr/lib/
ln -s libcrypto.so.0.9.8 libcrypto.so.4
ln -s libssl.so.0.9.8 libssl.so.4
```

trus sekarang coba jalankan lagi /etc/init.d/fms start dan seharusnya sekarang semuanya sudah berjalan dengan baik :)
