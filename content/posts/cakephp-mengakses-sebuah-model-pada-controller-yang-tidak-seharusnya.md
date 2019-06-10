+++
date = "2009-02-15"
slug = "2009/02/15/cakephp-mengakses-sebuah-model-pada-controller-yang-tidak-seharusnya"
title = "'CakePHP : Mengakses sebuah model pada controller yang berbeda'"
Categories = ["CakePHP"]
Tags = ["CakePHP", "programming"]
+++

Dalam CakePHP biasanya sebuah model - view - controller pasti saling berhubungan dan mempunyai nama yang mirip.

Contohnya sebuah tabel users mempunyai model yang bernama _user_, controller bernama _users_controller_, dan folder view yang bernama_ user_.

Tapi permasalahannya adalah terkadang kita harus mengakses model lain tetapi controller tersebut tidak mempunyai relasi sama sekali dengan model / tabel ini.

Sebagai contoh lagi misalnya kita ingin pada_ users_controller_ dapat melakukan query pada tabel _items_, padahal tabel users sama sekali tidak punya relasi dengan tabel items.

Ada beberapa cara yang dapat dilakukan untuk mensolusikan hal tersebut :

  1. Pada _users_controller_ kita dapat menambahkan variable baru yaitu _$uses = array('User','Item'); _dengan melakukan hal itu maka kita dapat melakukan query seperti biasa ( _$this->Item->find('all'); )_

  2. Satu cara lagi lebih praktis dilakukan dan bisa lebih fleksibel dilakukan yaitu dengan menggunakan _ClassRegistry. _Jadi tanpa harus menambahkan variable kita cukup melakukan pencarian ( contoh : _$items = ClassRegistry::init('Item')->find('all'); )_.

Itulah 2 cara yang dapat dilakukan jika anda ingin melakukan akses model yang sama sekali tidak ada relasi, tetapi jika anda terpaksa melakukan hal ini mungkin ada yang salah terjadi pada rancangan database anda karena rancangan database yang baik tidak seharusnya dapat melakukan query untuk database yang tidak saling berkaitan.

Tapi lebih baik berjaga-jaga siapa tahu anda mendapatkan project dimana anda harus menggunakan rancangan database yang sudah ada ( dan ternyata rancangan database tersebut kacau ). Ibarat kata pepatah sedia payung sebelum hujan.
