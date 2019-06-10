+++
date = "2009-07-23"
slug = "2009/07/23/koneksi-ke-microsoft-sql-server-dengan-php-di-freebsd"
title = "Koneksi ke Microsoft SQL Server dengan PHP di FreeBSD"
Categories = ["Unix and Linux"]
Tags = ["freebsd", "freetds", "microsoft", "mssql", "PHP", "sql server", "Ubuntu"]
+++

Beberapa hari yang lalu gwa melakukan perpindahan server Binus Access ke server baru yang menggunakan FreeBSD ( sebelumnya menggunaka Ubuntu Server 8.04 ). Setelah melakukan konfigurasi-konfigurasi dan beberapa persiapan yaitu :

  * Backup database dan file website Binus Access
	
  * Konfigurasi Nginx ( web servernya ganti Nginx ) agar bisa membaca mod_rewrite
	
  * Setting NFS dari server asterix ke server Binus Access
	
  * Setting IP

  * Beberapa settingan kecil lainnya

Jadi setelah dirasa semua persiapan sudah kelar, akhirnya perpindahan server dilakukan yaitu mencabut kabel LAN di server lama dan mencoloknya di server baru ( yap pindahin server cuma begitu saja ). Nah setelah gwa melakukan perpindahan server gwa pun mencoba semua fitur-fitur yang ada di binus-access satu persatu apakah ada yang ga jalan. Ternyata eh ternyata pas gwa tes registrasi untuk user baru terjadilah error dimana yang kalau gwa telusuri dikarenakan server tersebut tidak dapat mengakses server binusmaya ( menggunakan mssql ).

Jadi gwa pun mulai mencek dengan menggunakan phpinfo(); apakah extension mssql sudah terinstall di server FreeBSD tersebut atau blum ( karena seingat gwa pas nginstall php-fpm extension mssql sudah gwa aktifkan ), pas gwa cek ternyata extension mssql sudah terinstall dengan benarnya ( berarti tidak ada kesalahan dengan extension mssql.

Setelah itu gwa pun mulai searching di google dan akhirnya ketemu sebuah artikel yang menyebutkan tentang FreeTDS, gwa sih kurang ngerti juga tentang FreeTDS tapi kalau artikel itu bilang kalau mau connect mssql menggunakan FreeBSD harus menggunakan FreeTDS ini. Oleh karena itu tanpa banyak cing cong langsung saja gwa install FreeTDS lewat ports FreeBSD, neh syntaxnya :
    
``` bash
cd /usr/ports/databases/freetds
make install clean
```

Setelah menginstall FreeTDS langsung saja config freetds.confnya yang terletak di **/usr/local/etc/freetds.conf ** ini isinya config freetds gwa :

    
``` apache    
#
#
#   $Id: freetds.conf,v 1.11 2005/12/05 21:34:12 freddy77 Exp $
#
# The freetds.conf file is a replacement for the original interfaces
# file developed by Sybase.  You may use either this or the interfaces
# file, but not both.
#
# FreeTDS will search for a conf file in the following order:
#
#     1) check if a file was set programatically via dbsetifile() and
#        is in .conf format, if so use that,
#
#     2) otherwise, if env variable FREETDSCONF specifies a properly 
#        formatted config file, use it,
#
#     3) otherwise, look in ~/.freetds.conf,
#
#     4) otherwise, look in @sysconfdir@/freetds.conf
#
# If FreeTDS has found no suitable conf file it will then search for
# an interfaces file in the following order:
#
#     1) check if a file was set programatically via dbsetifile() and 
#        is in interfaces format, if so use that,
#
#     2) look in ~/.interfaces
#
#     3) look in $SYBASE/interfaces (where $SYBASE is an environment
#        variable)
#
# Only hostname, port number, and protocol version can be specified
# using the interfaces format.
#
# The conf file format follows a modified Samba style layout.  There
# is a [global] section which will affect all database servers and
# basic program behaviour, and a section headed with the database
# server's name which will have settings which override the global
# ones.
#
# Note that environment variables TDSVER, TDSDUMP, TDSPORT, TDSQUERY, 
# and TDSHOST will override values set by a .conf or .interfaces file.
#
# To review the processing of the above, set env variable TDSDUMPCONFIG
# to a file name to log configuration processing.
#
# Global settings, any value here may be overridden by a database
# server specific section
[global]
        # TDS protocol version
  tds version = 4.2

;	initial block size = 512

  # uses some fixes required for some bugged MSSQL 7.0 server that
  # return invalid data to big endian clients
  # NOTE TDS version 7.0 or 8.0 should be used instead
;	swap broken dates = no
;	swap broken money = no

  # Whether to write a TDSDUMP file for diagnostic purposes
  # (setting this to /tmp is insecure on a multi-user system)
;	dump file = /tmp/freetds.log
;	debug flags = 0xffff

  # Command and connection timeouts
;	timeout = 10
;	connect timeout = 10
  
  # If you get out of memory errors, it may mean that your client
  # is trying to allocate a huge buffer for a TEXT field.  
  # (Microsoft servers sometimes pretend TEXT columns are
  # 4 GB wide!)   If you have this problem, try setting 
  # 'text size' to a more reasonable limit 
  text size = 64512

# This is a Sybase hosted database server, if you are directly on the
# net you can use it to test.
[JDBC]
  host = 192.138.151.39
  port = 4444
  tds version = 5.0

# The same server, using TDS 4.2.  Used in configuration examples for the
# pool server, since the pool server supports only TDS 4.2.
[JDBC_42]
  host = 192.138.151.39
  port = 4444
  tds version = 4.2

# The client connecting to the pool server will use this to find its
# listening socket.  This entry assumes that the client is on the same
# system as the pool server.
[mypool]
  host = 127.0.0.1
  port = 5000
  tds version = 4.2

# A typical Microsoft SQL Server 7.0 configuration	
;[MyServer70]
;	host = ntmachine.domain.com
;	port = 1433
;	tds version = 7.0

# A typical Microsoft SQL Server 2000 configuration
[stored]
  host = 10.21.50.16
  port = 1433
  tds version = 8.0
  
# A typical Microsoft SQL Server 6.x configuration	
;[MyServer65]
;	host = ntmachine.domain.com
;	port = 1433
;	tds version = 4.2
```
jadi buat settingan mssql buat server binusmaya itu gwa letakin di bagian ini :

``` apache
# A typical Microsoft SQL Server 2000 configuration
[stored]
  host = xx.xx.xx.xx
  port = 1433
  tds version = 8.0
```

ganti tulisan xx.xx.xx.xx dengan ip server SQL Server nya. Nah sekarang saatnya mencoba melakukan koneksi ( ada sedikit perbedaan cara melakukan koneksi ) begini contoh codingnya dalam PHP :

    
``` php    
$host = "stored";
$user = "yourusername";
$pass = "yourpassword";
$db = mssql_connect($host,$user,$pass) or die ("Unable to connect to mssql databases");
```

Jadi perbedaannya adalah $host yang harus diisi dengan nama yang ada set di freetds.conf tadi, jadi jika pada freetds.conf ada menset namanya menjadi "mssql" maka pada host anda ubah menjadi "mssql". Kira-kira begitulah caranya yang cukup membuat gwa pusing selama 2 jam mencari-cari caranya. Lanjut ngejunk lagi ah :P
