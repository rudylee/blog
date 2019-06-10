+++
date = "2009-10-19"
slug = "2009/10/19/hotlinking-protection-di-web-server-apache"
title = "Hotlinking protection di web server Apache"
Categories = ["Research", "Unix and Linux"]
Tags = ["Add new tag", "Apache", "Bee Watch", "Binus Access", "binus-access.com", "fms", "hotlink protection", "Hotlinking", "Marketing", "TV Online", "Unix and Linux"]
+++

Hari ini gwa disibukkan dengan berbagai banyak kerjaan, entah kenapa kalau masuk kantor itu kerjaan tiba-tiba aja datang bertubi-tubi. Tapi kerjaan utama yang gwa lakukan hari ada memproteksi server Bee Watch. 

Yah, seperti yang kita ketahui bersama bahwa Bee Watch sangat menjadi incaran untuk di-embed ke web-web marketing kelas teri. Dimana siaran Bee Watch ( TV Online) digunakan sebagai penarik traffic ke website mereka dan di website mereka diletakkan bermacam-macam iklan entah darimana datangnya. Ada yang isinya iklan Joko Susilo lah, ada iklan google adsense la, dan iklan2 norak lainnya. Dan yang paling membuat gw prihatin adalah design website yang sangat kampungan dan acak-acakan ( sory kalo ini gwa ngomong jujur ).  

Selama ini gwa telah melakukan berbagai macam proteksi terhadap Bee Watch. Mulai dari proteksi dari FMS nya, random folder tempat simpan playernya , dan yang terakhir memasang firewall. Tapi ternyata memang dasar maling, tetep saja mereka selalu menemukan cara untuk menembus pertahanan yang gwa buat.

Akhirnya gwa memutuskan membuat hotlink protection di web server Apache gwa dengan menggunakan .htaccess. Mungkin ada yang bertanya-tanya sebenarnya apa itu hotlink. Hotlink itu adalah sebuah istilah yang digunakan ketika sebuah website A yang menghosting katakanlah sebuah gambar yang berukuran 100 MB, kemudian secara tiba-tiba ada website B yang meng-link gambar tersebut ke website milik pribadinya untuk kepentingan dia sendiri.

Ketika ada user yang mengakses website B dan menampilkan gambar yang dihosting oleh website A. Tentu saja hal itu merugikan website A dimana bandwidth yang digunakan adalah bandwidth website A, sementara website B cuma menikmati hasilnya tanpa harus kehilangan bandwidth yang berharga.

Hal inilah yang terjadi dengan Bee Watch dimana ada beberapa website yang tidak bertanggung jawab dengan sengaja melakukan embed siaran Bee Watch untuk menarik traffic ke website mereka. Dan setelah googling-googling dan stress selama 1 jam memikirkan bagaimana cara mem-ban website tersebut akhirnya gwa menemukan sebuah fitur dari web apache yaitu disable hotlinking dengan .htaccess.

Jadi konsepnya sangatlah simple dimana dengan menggunakan script .htaccess kita untuk mendisable semua akses ke file-file kita ( contoh : gambar .gif, .jpg, .png atau .swf ) sehingga hanya beberapa url saja yang telah kita allow dapat mengakses file tersebut ( dalam kasus ini gwa hanya mengallow domain binus-access.com dan 202.58.181.204 ).

Jadi step-stepnya kira begini :

  * Generate file .htaccess di web [ini](http://tools.dynamicdrive.com/userban/)
	
  * Upload file .htaccess ke root webserver kita ( misalnya /var/www ).
	
  * Testing hotlinking dari lokal

Jika benar maka seharusnya kita tidak dapat mengakses content website kita dari localhost. Kira-kira begitulah salah satu web security yang sangat penting jika kita ingin memproteksi website kita dari tangan-tangan jahil. Selamat mencoba :)
