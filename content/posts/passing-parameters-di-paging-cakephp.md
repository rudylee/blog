+++
date = "2009-10-20"
slug = "2009/10/20/passing-parameters-di-paging-cakephp"
title = "Passing parameters di paging CakePHP"
Categories = ["CakePHP"]
Tags = ["CakePHP", "coding", "limit", "pagination", "paging"]
+++

Sekian lama gwa ga sentuh2 CakePHP lagi ternyata sekarang ada kesempatan lagi buat megang CakePHP, ternyata setelah lama ga grepe2 CakePHP banyak codingan dan syntax2 yang gwa lupa dan salah satunya ada passing parameter ketika melakukan paging dan juga melimit jumlah row setiap halamannya.

jadi tanpa banyak cing cong seperti biasanya langsung saja ke codingan aja deh. Ceritanya gwa punya method dalam controller seperti ini.

``` php    
function index($id = null) {
  if(!$id) {
    $this->Session->setFlash(__('Invalid Question.', true));
  }
  else {
    $this->set('passedArgs',$id);
    $this->set('questions', $this->paginate(array('group_id' => $id)));
  }
}
```

Jadi kalau dilihat dari method tersebut terlihat bahwa gwa mempassing parameter ke dalam method indexnya, dan gwa menggunakan parameter tersebut dalam paging gwa. Oleh karena itu gwa membuat satu variable lagi bernama **passedArgs** untuk menyimpan parameter yang ingin gwa passing ke dalam url paging nantinya ( dalam hal ini id yang ingin gwa passing ).

Setelah itu akan menambah codingan ke dalam viewnya yaitu

``` php    
counter(array(
'format' => __('Page %page% of %pages%, showing %current% records out of %count% total, starting on record %start%, ending on %end%', true)
));
$paginator->options(array('url'=>$this->passedArgs));
```

Jadi kita hanya perlu menambah codingan $paginator->options yang di dalamnya kita letakkan variable yang ingin kita passing. Mungkin pada bingung kenapa gwa harus passing variable itu ke dalam halaman paging, jika anda bingung berarti anda harus belajar banyak lagi :)

Sekalian bonus biar ntar kalo lupa bisa ingat :
    
``` php
var $paginate = array(
  'limit'	=> 10
);
```

Code di atas buat limit jumlah item dalam 1 page, diletakkannya di dalam controller. Semoga membantu :D
