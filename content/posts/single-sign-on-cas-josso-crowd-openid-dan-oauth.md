+++
date = "2009-06-04"
slug = "2009/06/04/single-sign-on-cas-josso-crowd-openid-dan-oauth"
title = "Single Sign On, CAS, Josso, Crowd, OpenID, dan OAuth"
Categories = ["Research"]
Tags = ["CAS", "OAuth", "OpenID", "Single Sign On", "SOAP", "SSO"]
+++

Karena banyak yang minta dikirimin skripsi, sekarang udah gwa upload skripsi gwa. Silakan di download [**Klik Disini**](http://blog.rudylee.com/content/softcover 27jan.doc)

Lagi pengen update blog, tapi bingung musti ngisi apa... pengen curhat tapi nanti pada tanya2 lagi... ya sudah lah daripada cerita-cerita ga jelas bagusan bahas tentang single sign on atau SSO...

Single sign on ini merupakan topik skripsi gwa tahun lalu... yah bisa dibilang semester kemarin secara gwa sedang menunggu wisuda hari sabtu ini... ( sambil menunggu bak cang juga dari pekanbaru... ea ).

Sebelum bahas kedalam-dalam bahas dolo deh pengertian dari Single Sign On. Sebenarnya gwa juga bingung musti mengartikan dalam kata-kata, intinya sih dengan single sign on kita dapat membuat user hanya perlu melakukan login sekali untuk dapat mengakses aplikasi-aplikasi ( dalam hal ini bisa saja web atau aplikasi desktop) yang berbeda dan yang tentu saja pada server yang berbeda... Kalau pengen tahu lebih jelas cek di wikipedia saja [http://en.wikipedia.org/wiki/Single_sign-on](http://en.wikipedia.org/wiki/Single_sign-on). Untuk contoh realnya bisa liat yahoo messenger, ketika kita login di yahoo messenger ketik kita masuk ke web mailnya untuk mengecek email, kita tidak perlu melakukan login lagi karena kita sudah login melalui yahoo messengernya. Jadi itu adalah salah satu contoh Single Sign On.

Nah, untuk membuat teknologi Single Sign On ini tidaklah sulit, karena sekarang telah tersedia banyak teknologi, framework yang open source dan commercial. Beberapa framework dan teknologi itu antara lain :

  * [Central Authentication Services](http://www.jasig.org/cas)

	
  * [Josso](http://www.josso.org)

	
  * [Crowd ( Comercial )](http://www.atlassian.com/software/crowd/)

	
  * [OpenID](http://openid.net/)

	
  * [OAuth](http://oauth.net/)

Dari beberapa pilihan tersebut yang sudah pernah gwa coba cuma CAS dan Josso. Pada akhirnya pilihan gwa jatuh kepada CAS. Alasan utama kenapa gwa memilih CAS sangatlah simple yaitu karena paling gampang dipakai...

Tapi walaupun gampang dipakai ternyata CAS cukup handal juga untuk dipakai sebagai framework Single Sign On. Buktinya adalah banyaknya plugin yang dapat membantu kita jika ingin mengintegrasikan CAS ke aplikasi web lain ( misalnya ingin mengintegrasikan aplikasi web ASP dengan aplikasi web PHP )... 

Jadi pada skripsi gwa, gwa diharuskan mengintegrasikan beberapa aplikasi web dan desktop antara lain portal ( menggunakan Joomla ), blog ( menggunakan wordpress MU ), messenger ( menggunakan spark ), dan forum ( menggunakan fireboard dan terintegrasi dengan joomla ). Sementara untuk databasenya sendiri menggunakan Open [Lightweight Directory Access Protocol](http://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) ( OpenLDAP )... 

Sebelum membahas lebih lanjut gwa akan menjelaskan sedikit tentang framework CAS ini dahulu. CAS adalah sebuah framework untuk Single Sign On yang dibuat dengan bahasa Java atau lebih tepatnya JSP. Jadi CAS ini dapat dikatakan sebuah aplikasi web yang digunakan untuk meng-handle autentikasi nantinya ( sebagai pintu gerbang autentikasi nantinya ). Oleh karena itu setiap kita ingin melakukan autentikasi maka kita akan diredirect ke server CAS ini dan baru nantinya akan diredirect kembali ke aplikasi.

Kemudian yang menjadi pertanyaannya adalah bagaimana caranya aplikasi dapat mengetahui bahwa user tersebut telah melakukan login atau tidak. Konsep kerja CAS sebenarnya menggunakan Ticket Granting dimana ketika user melakukan login, user akan diberikan ticket ( dalam hal ini tersimpan dalam cookies ) yang nantinya digunakan untuk mengautentikasikan user pada setiap aplikasinya. Jadi nantinya di setiap aplikasi akan dilakukan pengecekan dari ticket yang telah diberikan oleh CAS tersebut.

Mungkin nanti gwa bakal bikin tutorial untuk CAS ini karena ada rencana pengen nyoba-nyoba CAS versi terbaru. Tapi selain itu gwa juga pengen nyoba teknologi baru yang hampir mirip dengan SSO yaitu OpenID dan OAuth. Dari hasil membaca-baca sedikit gwa menarik kesimpulan bahwa OpenID dan OAuth adalah sebuah konsep dimana kita dapat menggunakan username kita di aplikasi lain tanpa aplikasi tersebut mengakses database username kita. Yah mungkin hampir mirip dengan konsep SOAP, tapi gwa sendiri belum mendalami SOAP, OpenID dan OAuth. Mungkin nanti gwa bakal posting hasil researchnya.

