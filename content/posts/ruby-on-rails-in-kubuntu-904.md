+++
date = "2009-11-23"
slug = "2009/11/23/ruby-on-rails-in-kubuntu-904"
title = "Ruby on Rails in Kubuntu 9.04"
Categories = ["Ruby on Rails"]
Tags = ["CakePHP", "coding", "kubuntu", "MVC", "Pengalaman", "ruby", "Ruby on Rails"]
+++

Beberapa hari ini gwa disibukkan mencoba menginstall Ruby on Rails ( RoR ). Sebenarnya sudah cukup lama pengen coba-coba Ruby on Rails, tapi sekarang baru ada semangat sama ada waktu buat nyoba-nyoba.

Menginstall Ruby on Rails ini dapat dibilang cukup memakan banyak waktu dikarenakan gwa menghabiskan 1 harian HANYA untuk install Kubuntu doank ( gara2 cd rom yang ga jelas ).

Jadi setelah gwa berhasil menginstall kubuntu ( yang tentu saja gwa selesaikan dalam waktu 1 hari ) gwa mulai menginstall Ruby on Rails. Mungkin masih pada bingung sebenarnya Ruby on Rails itu apaan. Ruby on Rails itu adalah sebuah framework untuk pembuatan website yang dibuat dengan menggunakan bahasa Ruby.

Apa istimewanya ? Kok semua sekarang pada ngomong Ruby on Rails mulu ? Kalau yang setau gwa Ruby on Rails adalah framework yang pertama kali menerapkan konsep MVC ( Model - View - Controller ) yang banyak diadopsi oleh framework-framework lain ( CakePHP, CI, Symfony, Spring, dll ). Selain itu Twitter juga menggunakan Ruby on Rails sebagai platform utamanya ( walaupun ada performance issue ).

Yah jadi langsung aja kita mulai step-step menginstall Ruby on Rails. Langkah-langkahnya sebenarnya terbagi dalam beberapa bagian yaitu :

  1. Menginstall package yang dibutuhkan oleh Ruby on Rails
	
  2. Menginstall database server yang mau digunakan
	
  3. Menginstall Ruby, Rubygem, dan yang terakhir Rails

Kelihatannya gampang menginstall Ruby on Rails, tetapi karena banyaknya dependency terhadap package membuat kita harus sering compile ulang Ruby ( mungkin yang pakai apt-get lebih gampang, tetapi sekarang kita akan mencoba install from source ).

Berikut biodata dari Ruby yang akan kita install :

  1. ruby-1.8.7-p174
	
  2. rubygems-1.3.5
	
  3. rubygems-1.3.5

Jadi sejauh pengalaman saya, beberapa package yang harus diinstall terlebih dahulu ( di Kubuntu ya, kalau distro lain ga ikutan ) adalah:
	
  1. Zlib
	
  2. Openssl
	
  3. Mysql dev ( jika ingin menggunakan mysql )


Kalau mau install zlib di kubuntu tinggal ketik aja
    
``` bash
sudo apt-get install zlib1g-dev
```

sementara untuk openssl ketik

``` bash    
sudo apt-get install libopenssl-ruby1.9
sudo apt-get install libssl-dev
```
    
untuk library openssl bisa disesuaikan dengan versi rubynya ( dan kalau mau gampang search aja di Software Management kubuntunya ). Setelah itu kita akan menginstall mysql-server ( karena gwa pakainya mysql ). Kalau misalnya anda tidak ingin menggunakan mysql juga tidak apa-apa, karena defaultnya ruby itu menggunakan sqllite.

untuk mysql saya menggunakan command ini

``` bash
sudo apt-get install mysql-server
```
    
sementara untuk library dev mysqlnya gwa menggunakan Software Management( jadi gwa ga gitu ingat packagenya yang mana ). Setelah selesai install mysqlnya kita tinggal download aja source Ruby dari website Ruby on Rails yaitu di [www.rubyonrails.org](http://www.rubyonrails.org) dan pilih menu download. Disana bakal ada tulisan **Source: Compile it yourself**, nah tinggal klik aja tulisan source nya dan anda sudah dapat sourcenya Ruby.

Langkah-langkahnya kira-kira begini :
	
  1. Selesai download copy aja file source Rubynya ke mana aja ( ex : /usr/local ) 
	
  2. Extract file source tadi ( tar xzvf rubygems-1.3.5.tgz ).
	
  3. kemudian masuk ke dalam folder yang sudah diextract tadi.
	
  4. Jalankan langkah untuk compile ( **./configure**, **make,** dan terakhir adalah **make install** ).
	
  5. gwa sempat mencoba menggunakan ./configure && make && make install tapi hasilnya tidak berhasil ( jadi kalau ada yang mau coba silakan saja, gwa sih pakai cara manual, jalanin satu2 ).

Nah setelah itu harusnya Ruby kita sudah terinstall, coba jalankan perintah ini :

``` bash
ruby -v atau ruby --version
```
    
Jgn pernah jalanin ruby -version karena akan muncul error message ( harus -- ). Kalau sudah terinstall harusnya muncul tulisan seperti ini :

``` ruby    
ruby 1.8.7 (2009-06-12 patchlevel 174) [i686-linux]
```

Nah kalau sudah benar lanjut ke step selanjutnya, kalau gagal coba debugging sendiri aja ya ( googling gitu ). Selanjutnya kita akan menginstall RubyGems atau bisa disebut sebagai Package Managernya Ruby ( mirip apt-get tapi punyanya Ruby ). Langkah-langkahnya :

  1. Masuk lagi ke website Ruby on Rails bagian download, [http://rubyonrails.org/download](http://rubyonrails.org/download)
	
  2. Cari bagian RubyGems dan pilih Download
	
  3. Untuk versi terserah pilih yang mana suka la, gwa mah ambil yang paling baru.
	
  4. Setelah download tinggal pindahin aja ke folder mana aja ( ex : /usr/local ).
	
  5. Extract lagi RubyGems nya ( tar xzvf rubygems-1.3.5.tgz )
	
  6. Masuk ke folder yang baru diextract tadi dan jalankan perintah **ruby setup.rb**
	
  7. Tunggu proses dan jika tidak terjadi error maka jalankan perintah **gem help**

Jika gem terinstall dengan benar maka harusnya muncul help tentang penggunaan gem. Sekarang kita akan menginstall rails, tetapi sebelum kita harus menginstall Rake.

``` bash    
gem install rake
```

Setelah selesai kita tinggal menginstall Rails dengan :
    
``` bash
gem install rails
```
    
Selesai menginstall rails seharusnya semua langkah sudah selesai, kita tinggal mengetes apakah Ruby on Rails berjalan dengan baik. Masuk ke folder tempat dimana anda akan menyimpan file website anda nanti ( ex: /home/rudy/ruby ). Kemudian ketik perintah ini :

``` bash    
rails blog -d mysql
```

Dari perintah diatas kita akan membuat folder dengan nama blog dan menggunakan koneksi mysql ( kalau ga pakai -d mysql, secara otomatis ruby akan membuat konfigurasi menggunakan sqllite ).

Masuk ke dalam folder blog tersebut, dan masuk ke dalam folder config dan cari file **database.yml**, kira-kira isinya begini :

``` yml    
# MySQL.  Versions 4.1 and 5.0 are recommended.
#
# Install the MySQL driver:
#   gem install mysql
# On Mac OS X:
#   sudo gem install mysql -- --with-mysql-dir=/usr/local/mysql
# On Mac OS X Leopard:
#   sudo env ARCHFLAGS="-arch i386" gem install mysql -- --with-mysql-config=/usr/local/mysql/bin/mysql_config
#       This sets the ARCHFLAGS environment variable to your native architecture
# On Windows:
#   gem install mysql
#       Choose the win32 build.
#       Install MySQL and put its /bin directory on your path.
#
# And be sure to use new-style password hashing:
#   http://dev.mysql.com/doc/refman/5.0/en/old-client.html
development:
  adapter: mysql
  encoding: utf8
  reconnect: false
  database: blog_development
  pool: 5
  username: root
  password:
  host: localhost

# Warning: The database defined as "test" will be erased and
# re-generated from your development database when you run "rake".
# Do not set this db to the same as development or production.
test:
  adapter: mysql
  encoding: utf8
  reconnect: false
  database: blog_test
  pool: 5
  username: root
  password:
  host: localhost

production:
  adapter: mysql
  encoding: utf8
  reconnect: false
  database: blog_production
  pool: 5
  username: root
  password: 
  host: localhost
```
    
ubah username dan password sesuai dengan settingan mysql anda. Kemudian keluar dari folder config dan jalankan perintah ini :
    
``` bash
rake db:create 
```
    
Jika benar maka database akan otomatis terbuat ( jika ada error message berarti ada package mysql yang belum terinstall dengan benar ). Lalu jalankan perintah ini lagi :

``` bash
script/generate controller home index 
```
    
tunggu sampai proses generate selesai ( jika ada yang error, yah anda tau sendiri lah, berarti ada package yang kurang ). Trus jalanin lagi perintah untuk jalanin webservernya :

``` bash    
script/server 
```
    
Jika benar maka akan ada proses menjalankan web servernya ( jgn diclose terminalnya karena akan membuat web server tersebut mati ). Untuk mengakses aplikasi Ruby on Rails yang baru dibuat, masuk ke web browser anda dan ketik

``` bash
http://localhost:3000/
```

Selamat, anda telah berhasil menginstall Ruby on Rails dan sekarang tinggal belajar configurasinya aja :D
