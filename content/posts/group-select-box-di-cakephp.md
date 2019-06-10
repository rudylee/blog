+++
date = "2009-11-02"
slug = "2009/11/02/group-select-box-di-cakephp"
title = "Group select box di CakePHP"
Categories = ["CakePHP"]
Tags = ["cake", "cake select box", "CakePHP", "coding", "helper", "PHP", "set::combine"]
+++

Grouping di dalam select box adalah hal yang gampang ketika kita menggunakan codingan php biasa, tetapi kalau sudah masuk ke dalam codingan CakePHP kita harus banyak membaca documentation untuk teknik2nya, tickets jika ada yang pernah menanyakan hal yang sama dan tentu saja API agar kita tahu fungsi dari method yang akan kita pakai.

Jadi sekarang kita akan membuat sebuah grouping dalam select box seperti dalam gambar di bawah ini :
[caption id="" align="alignnone" width="217" caption="CakePHP Group Select"]![CakePHP Group Select](http://blog.rudylee.com/content/group-select-box.jpg)[/caption]

Di dalam contoh diatas gwa menggunakan 3 buah table di antaranya table majors ( jurusan ), table faculties ( fakultas ) dan table levels ( untuk pembagian apakah dia D3/S1 ). Hal pertama yang harus kita lakukan adalah men-query isi table dari majors ( dalam hal ini gwa menggunakan ClassRegistry karena table majors tidak ada relation dengan controller gwa ) :

``` php    
$majors = ClassRegistry::init("Major")->find("all");
```
    
atau kalau punya relation / berada dalam controller sendiri

``` php
$majors = $this->Major->find("all");
```
    
Kemudian kita akan menggabungkan hasil query tersebut dan menyusunnya menjadi array yang jika kita masukkan ke dalam form helper maka akan secara otomatis menjadi select box yang tergroup. Kita akan menggunakan bantuan Set::combine untuk melakukan hal tersebut. Berikut contoh codingannya :

``` php
$majorsCombine = Set::combine($majors, "{n}.Major.id", array("%s - %s",
"{n}.Level.name", "{n}.Major.name"), "{n}.Faculty.name"); 
```
    
untuk penjelasan parameternya dapat dilihat di API CakePHP : <a href="http://api.cakephp.org/class/set#method-Setcombine">API CakePHP</a>
    
sedikit penjelasan tentang parameter yang gwa gunakan yaitu :
	
* $majorsCombine _Nama variable penampung._

* Set::combine _Nama method yang kita gunakan._

* $majors _Sumber data kita_

* {n}.Major.id _Path pertama atau biasanya nilai dari select box kita_

* array('%s - %s','{n}.Level.name', '{n}.Major.name') _Kalau ini path kedua yang berfungsi sebagai label dari isi select box kita, jika dilihat itu isinya ada level dan major jadi nanti keluarnya ( S1 - Teknik Informatika )_

* {n}.Faculty.name' _ini nama groupnya_

Selanjutnya tinggal digunakan saja di viewnya seperti ini :

``` php
$form->select("nama-form",$majorsCombine,null,null,"-- Pilih Jurusan Pertama --"); ?>
```

Penjelasannya kira-kira begini :
	
* $form->select _ini form helper yang kita gunakan_

* nama-form _nama form helper yang kita gunakan_

* $majorsCombine _sumber data_

* null,null,'-- Pilih Jurusan Pertama -- _parameter tambahan lagi_

Semoga membantu, silakan dicoba.. kalau ga jalan, dicoba lagi, kalau ga jalan juga ya sudah terima nasih aja :D
