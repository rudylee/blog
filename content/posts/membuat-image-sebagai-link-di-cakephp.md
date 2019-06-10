+++
date = "2009-11-02"
slug = "2009/11/02/membuat-image-sebagai-link-di-cakephp"
title = "Membuat image sebagai link di CakePHP"
Categories = ["CakePHP"]
Tags = ["CakePHP", "coding", "helper", "image"]
+++

Mungkin kita pernah membuat sebuah gambar menjadi sebuah link seperti untuk banner registrasi atau banner untuk iklan dan sebagainya.

Jika cara biasanya atau konvesional maka kita tinggal membuat seperti ini :

    
    
    <a href="http://xxx"><img src="path/images"></a>
    



Sementara dalam CakePHP ada cara yang lebih gampang atau mungkin bagi beberapa orang lebih susah, yaitu :

    
    
    link($html->image('/images/btn-register.png'), array('controller' => 'users','action' => 'add'),array('escape' => false)) ?>
    
    atau kira-kira susunannya seperti ini
    link($html->image('path-ke-image), array('controller' => 'nama-controller','action' => 'nama-action'),array('escape' => false)) ?>
    



Jadi kita menggunakan 2 buah helper yaitu link dan image dimana helper dari image kita letakkan di dalam helper link. Jangan lupa untuk menambahkan attribute **escape => false** atau gambar yang ingin anda tampilkan tidak akan muncul. Semoga bermanfaat :D
