+++
date = "2010-06-03"
slug = "2010/06/03/upload-file-in-cakephp-using-media-plugin"
title = "Upload file in CakePHP using Media Plugin"
Categories = ["CakePHP"]
Tags = ["auto increment", "basename", "cake", "CakePHP", "checksum", "component one", "control", "coupler", "file upload", "implementation", "inspiration", "many things", "media", "meta generator", "move uploaded file", "photos", "plugin", "private action", "several ways", "upload", "wiki"]
+++

There are many solutions to handle file upload in PHP, one of the common solutions is to create a custom action that will check the type of the file, size, validate whether the file name already exists or not, and the last thing is moving the file using move_uploaded_file(). However, it doesn't end when the files are in your server, after that you still need to write a function to delete the files, manipulate it if needed and so on.

I already tried several ways to handle upload file in CakePHP, from writing a private action in the app_controller and the last I write a component. 

I can upload file, delete file, check the file type using my Upload Component, but I realize that there are many things missing in my component. 

In searching for inspiration, I found CakePHP do have serveral plugins to handle File Upload and the features are beyond my component.

One of the plugin is [Media Plugin](http://github.com/davidpersson/media) by Davidpersson.

Using the plugin is quite easy, but the wiki and the CakeFest slide is not updated with the new configuration ( I am using v1.3alpha ), so you need to jumped in to the core and trying to understand the new configuration.

Basically the plugin consist of several behaviours :
	
  * Transfer
	
  * Polymorphic
	
  * Meta
	
  * Generator
	
  * Coupler

But in this post I will just cover the Transfer,Coupler and Meta behaviour because I only understand these behaviours. So lets go to the implementation part, here is my CakePHP and Media Plugin version :
	
  1. CakePHP 1.3.0
	
  2. Media Plugin 1.3 alpha

First you must create a table that has a 'file' field in it. Remember, the field must be named 'file' or the plugin won't working. Here is the example with my application :

``` sql
CREATE TABLE IF NOT EXISTS `photos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `file` varchar(255) NOT NULL,
  `dirname` varchar(255) NOT NULL,
  `basename` varchar(255) NOT NULL,
  `checksum` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;
```

The field that will be used by the plugin are file, dirname, basename, and checksum. But the three last fields is optional, so you can have it in your table or not (if you are using Coupler, and Meta behaviour you MUST add the there fields ). Next, bake the application ( I was using 'cake bake' command ).

After that grab the Media Plugin from the github and put it in the plugins folder of your application. Next you will need to include the plugin to your application, open your bootstrap.php / core.php and add this line in it :

``` php    
  require APP . 'plugins/media/config/core.php';
```

Then create the folder that will be used for storing the files. Go to your application folder in terminal and type this command ( ex: /var/www/sample ) :

``` bash    
  cake media init
```

The command will ask whether you want to create the directories or not, this is the print out of my terminal :

``` bash    
rudy@rudy-laptop:~/www/dummy$ cake media init
---------------------------------------------------------------
Media Shell
---------------------------------------------------------------
Do you want to create missing media directories now?
[n] > y
/dummy/webroot/media/                              [OK  ]
/dummy/webroot/media/static/                       [OK  ]
/dummy/webroot/media/static/aud                    [OK  ]
/dummy/webroot/media/static/css                    [OK  ]
/dummy/webroot/media/static/doc                    [OK  ]
/dummy/webroot/media/static/gen                    [OK  ]
/dummy/webroot/media/static/ico                    [OK  ]
/dummy/webroot/media/static/img                    [OK  ]
/dummy/webroot/media/static/js                     [OK  ]
/dummy/webroot/media/static/txt                    [OK  ]
/dummy/webroot/media/static/vid                    [OK  ]
/dummy/webroot/media/transfer/                     [OK  ]
/dummy/webroot/media/transfer/aud                  [OK  ]
/dummy/webroot/media/transfer/css                  [OK  ]
/dummy/webroot/media/transfer/doc                  [OK  ]
/dummy/webroot/media/transfer/gen                  [OK  ]
/dummy/webroot/media/transfer/ico                  [OK  ]
/dummy/webroot/media/transfer/img                  [OK  ]
/dummy/webroot/media/transfer/js                   [OK  ]
/dummy/webroot/media/transfer/txt                  [OK  ]
/dummy/webroot/media/transfer/vid                  [OK  ]
/dummy/webroot/media/filter/                       [OK  ]

/dummy/webroot/media/transfer/.htaccess is not in your webroot.
Remember to set the correct permissions on transfer and filter directory.
```

Change the permission of the folder so that the webserver can write in it :
    
``` bash
  chown -R www-data webroot/media
```

Configure the 'Photo' model like this :
    
``` php
class Photo extends AppModel {
    var $name = 'Photo';
    var $displayField = 'title';
    var $actsAs = array('Media.Transfer','Media.Coupler','Media.Meta');
    var $validate = array(
        'file' => array(
            'mimeType' => array(
                'rule' => array('checkMimeType', false, array ( 'image/jpeg', 'image/png'))
        ),
        'size' => array(
            'rule' => array('checkSize' , '5M')
        )
    ));
}
    


As you can see, I added 3 behaviors ( Transfer, Coupler and Meta ). The transfer behavior is used for uploading, moving and validating the file. The coupler is for deleting the file ( it will automatically delete the file if you delete a record associated with it and also will automatically add the value in dirname and basename ), the last thing that it will do is adding the meta description to the table ( checksum ).

Edit the add.ctp and adding the 'type' => 'file' in the $this->Form->create and the $this->Form->input('file') so the form can handle file upload. In the controller you don't need to change anything because the behavior automatically handle the validation, the path and moving the file. this is my controller :

``` php 
Photo->recursive = 0;
    $this->set('photos', $this->paginate());
}
    
function view($id = null) {
    if (!$id) {
        $this->Session->setFlash(sprintf(__('Invalid %s', true), 'photo'));
        $this->redirect(array('action' => 'index'));
    }
    $this->set('photo', $this->Photo->read(null, $id));
}

function add() {
    if (!empty($this->data)) {
        $this->Photo->create();
        if ($this->Photo->saveAll($this->data)) {
            $this->Session->setFlash(sprintf(__('The %s has been saved', true), 'photo'));
            $this->redirect(array('action' => 'index'));
        } else {
            $this->Session->setFlash(sprintf(__('The %s could not be saved. Please, try again.', true), 'photo'));
        }
    }
}

function edit($id = null) {
    if (!$id && empty($this->data)) {
        $this->Session->setFlash(sprintf(__('Invalid %s', true), 'photo'));
        $this->redirect(array('action' => 'index'));
    }
    if (!empty($this->data)) {
        if ($this->Photo->save($this->data)) {
            $this->Session->setFlash(sprintf(__('The %s has been saved', true), 'photo'));
            $this->redirect(array('action' => 'index'));
        } else {
            $this->Session->setFlash(sprintf(__('The %s could not be saved. Please, try again.', true), 'photo'));
        }
    }
    if (empty($this->data)) {
        $this->data = $this->Photo->read(null, $id);
    }
}

function delete($id = null) {
    if (!$id) {
        $this->Session->setFlash(sprintf(__('Invalid id for %s', true), 'photo'));
        $this->redirect(array('action'=>'index'));
    }
    if ($this->Photo->delete($id)) {
        $this->Session->setFlash(sprintf(__('%s deleted', true), 'Photo'));
        $this->redirect(array('action'=>'index'));
    }
        $this->Session->setFlash(sprintf(__('%s was not deleted', true), 'Photo'));
        $this->redirect(array('action' => 'index'));
    }
}
?>
```
    
and this is my add view :

``` php
echo $this->Form->create('Photo',array('type' => 'file'));
echo $this->Form->input('title');
echo $this->Form->input('file',array('type' => 'file'));
echo $this->Form->end(__('Submit', true));
```

Now you are ready to uploading files, deleting files, and validate them in the model ( for validation you can see the wiki in the github for complete validation ). That's all :D
