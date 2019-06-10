+++
date = "2013-02-02"
slug = "2013/02/02/select2-ajax-auto-complete-with-cakephp-2-0"
title = "Select2 AJAX Auto Complete with CakePHP 2.0"
Categories = ["CakePHP"]
+++

## Demo : [http://cbunny2.rudylee.com/users/select2](http://cbunny2.rudylee.com/users/select2)
Source : [https://github.com/rudylee/cbunny](https://github.com/rudylee/cbunny)


In this post, I'll explain how to use [Select2](http://ivaynberg.github.com/select2/) inside CakePHP. We will avoid using any helpers and rely on jQuery + Javascript. Before we start, I presume you have downloaded Select2 and included the Javascript and CSS files inside your layout. Thus, I won't explain how to import Select2 library into your CakePHP app ( you can download my cbunny app from Github if you are lost ).

So the first step is to create controller that will contain our Select2 search box. In this tutorial, I'll create users controller and one action to put the select2 search box. Here is the snippet of my code :

``` php    
public function select2() {
    $this->User->recursive = 0;
    $this->set('users', $this->paginate());
}
```


After this you can create the view ( View/Users/select2.ctp ). Here is my view code :

``` html    
<div class="row">
    <div class="span12">

    <!-- Select2 Auto Complete -->
    <div class="pull-right">
        <input type="text" id="user-select2">
    </div>

    <h2><?php echo __('Users');?></h2>
    <table class="table"cellpadding="0" cellspacing="0">
        <thead>
            <tr>
                <th><?php echo $this->Paginator->sort('id');?></th>
                <th><?php echo $this->Paginator->sort('username');?></th>
                <th><?php echo $this->Paginator->sort('password');?></th>
                <th><?php echo $this->Paginator->sort('created');?></th>
                <th><?php echo $this->Paginator->sort('modified');?></th>
                <th class="actions"><?php echo __('Actions');?></th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($users as $user): ?>
            <tr>
                <td><?php echo h($user['User']['id']); ?> </td>
                <td><?php echo h($user['User']['username']); ?> </td>
                <td><?php echo h($user['User']['password']); ?> </td>
                <td><?php echo h($user['User']['created']); ?> </td>
                <td><?php echo h($user['User']['modified']); ?> </td>
                <td class="actions">
                    <?php echo $this->Html->link(__('View'), array('action' => 'view', $user['User']['id'])); ?>
                </td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</div>
```


If you look at 5-7 you'll notice that I have input element with id element user-select2. We will use the ID inside our jQuery to initiate the Select2. The next step after this is to create a Javascript object to store the dynamic app path. Add this snippet of code into your layout file ( default.ctp ).

``` php  
$cbunny = array(
    'APP_PATH' => Router::url('/',true)
);
echo $this->Html->scriptBlock('var CbunnyObj = ' . $this->Javascript->object($cbunny) . ';');
```


You can change the $cbunny and CBunnyObj variable name to resemble your app name. However, the rest of the code has to be same as above. This snippet of code will create Javascript object which contains the root URL path of CakePHP.

After we have the Javascript object, we will create jQuery code to create Select2 search box, process AJAX request and handle the respond. I'll start with creating cbunny.js file inside my webroot folder and add the file in my layout file. Here is the code :

``` javascript  
/*global $, document, CbunnyObj */
$(document).ready(function () {

  $('#user-select2').select2({
    placeholder: "Search user auto complete",
    minimumInputLength: 1,
    ajax: {
      url: CbunnyObj.APP_PATH + 'users/search',
      dataType: 'json',
      data: function (term, page) {
        return {
          q: term
        };
      },
      results: function (data, page) {
        return { results: data };
      }
    }
  });

});
```


I'll explain the Javascript code a little bit. Line 4-19 contain the definition of Select2 library. You can see we have ajax definition on line 7 which will perform AJAX request to  CbunnyObj.APP_PATH + 'users/search'. CbunnyObj is javascript object variable that we have defined before and will translate into your CakePHP App path ( ex: http://cbunny.rudylee.com ). I believe you understand the rest of the code as I just copied it from Select2 website.

After this, our last step is to create action + view to handle the AJAX request. So we are going back to Users controller and add new action called 'search'. Here is my 'search' action code :

``` php 
public function search() {
    $this->autoRender = false;

    // get the search term from URL
    $term = $this->request->query['q'];
    $users = $this->User->find('all',array(
        'conditions' => array(
            'User.username LIKE' => '%'.$term.'%'
        )
    ));

    // Format the result for select2
    $result = array();
    foreach($users as $key => $user) {
        $result[$key]['id'] = (int) $user['User']['id'];
        $result[$key]['text'] = $user['User']['username'];
    }
    $users = $result;

    echo json_encode($users);
}
```


On line 5, we grab the search query term from the URL and store into $term variable. After that, we will perform normal query to the table. When we get the result, we won't be able to use it straight away. We will have to reformat it so it can be readable by Select2. On line 12-17 we basically iterate through the $users variable and create new associative array which has id and text as their key.

That's it for the tutorial. If you are confuse, feel free to write comment below and I'll be happy to answer them.
