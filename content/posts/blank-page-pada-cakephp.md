+++
date = "2009-05-18"
slug = "2009/05/18/blank-page-pada-cakephp"
title = "Blank page pada CakePHP"
Categories = ["CakePHP"]
Tags = ["blank", "CakePHP", "PHP"]
+++

Hari ini gwa mencoba memindahkan sebuah project yang dibuat dengan menggunakan CakePHP ke komputer lain. Persiapan standard seperti mencopy folder project dan nge-dump file database sudah dilakukan. Trus file-file tersebut dimasukkan ke dalam flash disk untuk dipindahkan.

Tetapi ternyata semua tidak berjalan mulus seperti yang gwa kira. Setelah selesai mengcopy file tersebut ke dalam komputer yang lain, ketika ingin membuka halaman cakephp ternyata hanya halaman kosong saja yang terbuka.

Pertama kali kecurigaan dimulai dari webserver dan settingan PHP. Soalnya di komputer yang ini gwa menggunakan Lighttpd sementara di komputer di kosan pakai apache, jadi mulai deh googling mencari apakah ini salah dari webserver ( hasilnya didapat kalau ingin mencari error maka dapat melihat dari file log yang ada di folder log ).

Setelah mengutak-atik file conf nya Lighttpd dan melihat file log, ternyata tidak ada yang aneh dengan settingan lighttpd dan settingan php.ini nya. Kemudian kecurigaan menuju ke CakePHP nya, jadi mulai deh search di google tentang CakePHP blank page. Dan ternyata ga lama mencari-cari akhirnya ketemu solusinya. Ternyata solusinya gampang cukup delete file cache yang ada folder tmp/cache dan ternyata hasilnya... langsung bisa kebuka webnya :D

jadi kalau copy file cakephp ke server baru delete aja cachenya biar aman, supaya ga page kosong jadinya :D
