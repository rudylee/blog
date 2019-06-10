+++
date = "2009-04-18"
slug = "2009/04/18/review-cakephp"
title = "Review CakePHP"
Categories = ["CakePHP", "Reviews"]
Tags = ["cake", "element", "helper", "PHP"]
+++

Setelah sekian lama ga update blog, akhirnya update blog lagi deh... Untuk kali ini ga bakalan cerita-cerita yang aneh-aneh ataupun yang lucu-lucu... soalnya emang lagi ga ada kejadian yang benar-benar "klik" yang bisa diceritakan ( beberapa hari ini semua terasa semu hix ).

Jadi kali ini gwa akan melakukan review terhadap framework PHP yang sudah gwa pelajari kurang lebih 5 bulan lamanya yaitu CakePHP. Selama 5 bulan ini gwa lewati dengan mempelajari CakePHP, dari baca ebook, nonton video tutorial sampai tanya-tanya sama orang-orang di channel #cakephp di irc.freenode.net.

Dalam waktu 5 bulan ini sudah banyak yang gwa pelajari dari CakePHP, tapi tetep masih lebih banyak lagi yang harus dipelajari dari CakePHP... Jadi intinya gwa bakal sharing apa yang sudah gwa dapatkan setelah lebih kurang 5 bulan mempelajari CakePHP ( FYI, gwa belom pernah pakai framework lain selain CakePHP ).

Salah satu hal yang gwa dapatkan dari mempelajari CakePHP adalah mengerti arsitektur MVC ( Model View Controller ). Untuk yang pengen tahu lebih banyak tentang MVC dapat dibaca di [http://en.wikipedia.org/wiki/Model-view-controller](http://en.wikipedia.org/wiki/Model-view-controller).

Tapi gwa coba rangkum beberapa hal yang gwa mengerti tentang MVC, dalam pemprograman MVC seluruh program dibagi menjadi 3 bagian utama yaitu Model ( berhubungan dengan database ), Controller ( berhubungan dengan logic ), View ( berhubungan dengan tampilan program).  Jadi jika pada pemprograman procedural atau pemprograman barbar kita bagi dalam function-function, maka pada MVC kita harus membaginya menjadi 3 bagian besar.

Jika kita ingin melakukan query,validasi, edit data kita masukkan ke dalam Model. Kalau kita ingin mengatur aliran data maka kita memasukkannya ke dalam Controller, dan yang terakhir kali jika kita ingin mengatur tampilan dari program kita ( designnya ) maka kita atur di View. 3 hal tersebut saling berhubungan dan mempunyai peran masing-masing.

Selain MVC tentu saja gwa banyak mempelajari penggunaan dari CakePHP itu sendiri. Penggunaan Helper-helper seperti AJAX, Session, Javascript, dan HTML. Jadi CakePHP secara default sudah menyediakan beberapa helper. Helper itu sendiri adalah sebuah class yang dapat digunakan untuk membantu kita dalam membuat aplikasi sesuai dengan helper yang kita gunakan. Jadi jika kita ingin membuat sebuah website yang menggunakan AJAX, kita dapat menggunakan AJAX helper yang dapat meringankan tugas kita dalam membuat aplikasi AJAX itu. Sama halnya jika kita ingin membuat session maka kita dapat menggunakan session helper untuk membantu kita mengatur session di CakePHP.

Selain helper dikenal juga istilah element di dalam CakePHP. Element disini bukan berarti elemen air, elemen api, elemen tanah. Element di dalam CakePHP itu lebih dapat diartikan sebagai view yang reuseable. Jadi misalnya kita mempunyai sebuah form dan kita ingin membuat form tersebut di 2 view yang berbeda maka kita dapat menggunakan element. Jadi kita tidak perlu membuat ulang kembali form tersebut di 2 view yang berbeda, cukup buat sebuah element dan panggil element tersebut di 2 view itu.

[caption id="" align="alignnone" width="550" caption="Paging dengan element"]![Paging dengan element](http://blog.rudylee.com/content/paging.jpg)[/caption]

Dan satu hal lagi yang harus diperhatikan dalam merancang sebuah aplikasi dengan menggunakan konsep MVC adalah Model sebaiknya lebih memiliki banyak method dibandingkan controller. Hal itu dikarenakan konsep dari OOP itu sendiri yaitu 'reuseable'.

Jadi gwa bisa menyimpulkan selama 5 bulan apa saja keuntungan yang didapatkan dari mempelajari CakePHP
	
  * Mengerti konsep MVC.
	
  * Waktu untuk mendevelop program menjadi lebih cepat.
	
  * Source code menjadi lebih terstruktur.
	
  * Kemampuan berbahasa inggris meningkat ( banyak baca cookbook + tanya2 pakai bahasa inggris wakaka.

Walaupun gwa tidak menampik adanya kerugian-kerugian yang didapatkan dari mempelajari CakePHP, ini beberapa kerugian tersebut :
	
  * Harus belajar kembali karena dengan menggunakan framework tentu saja kita harus mempelajari API yang sudah tersedia.
	
  * Aplikasi jadi lebih lemot.
	
  * Jadi makin malas karena sudah dimanjakan dengan fitur-fitur walaupun tidak semalas  karena menggunakan CMS
	
  * Makin lupa syntax2 PHP yang dasar karena keseringan menggunakan syntax CakePHP

Tapi walaupun begitu semua kekurangan itu tertutupi oleh kelebihan-kelebihan yang didapatkan dari mempelajari CakePHP tersebut. Yah jelas, kalau banyak ruginya napaen gwa capek-capek belajar framework. Mungkin ada yang beranggapan kalau menggunakan framework itu sendiri dapat memperbodoh diri sendiri, dan gwa pun tidak menampik hal tersebut. 

Tapi gwa menganalogikan mempelajari framework ini seperti sedang memasak mie goreng. Bedanya jika kita menggunakan framework maka kita menggunakan mie yang sudah dijual di pasaran tanpa kita tahu cara membuat mie tersebut. Sementara orang yang tidak menggunakan framework adalah orang yang membuat mienya sendiri.

Pertanyaannya adalah apakah mie goreng yang dibuat dengan mie jualan di pasar pasti lebih enak daripada mie yang dibuat sendiri ? bagaimana sebaliknya ? tentu saja jawabnya tergantung dari banyak faktor ( bisa kualitas mie, bisa kemampuan orang yang memasak ). 

Sama halnya dalam menggunakan framework, seberapa bagusnya aplikasi kita bukan saja ditentukan dari framework apa yang kita gunakan, bukan juga ditentukan dari apakah kita menggunakan framework atau tidak. Tetapi juga ditentukan dari kemampuan orang tersebut, karena di mata client tetap saja yang dilihat itu adalah hasil jadinya, bukan codingannya ( kebanyakan client kan ga ngerti2 banget :P ). Jadi client mana mo tau itu mie hasil buat sendiri ato hasil beli di pasar, yang mereka tahu cuma "mie ini enak", "mie ini ga enak". Udah itu aja, simple sekali kan ?

Yah sebenarnya kalau mau didebatkan lagi sebenarnya banyak yang bisa didebatkan tapi intinya sekarang gwa malas nulis panjang-panjang dan juga tentu saja gwa mendukung semua orang untuk mempelajari framework. Kenapa ? karena sekarang persaingan sudah semakin ketat, kita sekarang membuat aplikasi semakin mudah dan semakin cepat. Ibarat kata pepatah "Siapa cepat dia dapat". Sekarang itu ada di tangan anda, apakah anda ingin memakai mie yang dijual atau buat mie sendiri :P hohoho yang penting untuk sekarang 5 star buat CakePHP deh :)
