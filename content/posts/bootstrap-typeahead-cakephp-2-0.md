+++
date = "2013-02-02"
slug = "2013/02/02/bootstrap-typeahead-cakephp-2-0"
title = "Bootstrap Typeahead CakePHP 2.0"
Categories = ["CakePHP"]
+++

## 
Demo : [http://cbunny2.rudylee.com/users/typeahead](http://cbunny2.rudylee.com/users/typeahead)
Source : [https://github.com/rudylee/cbunny](https://github.com/rudylee/cbunny)



In this post, I'll explain how to integrate Twitter Bootstrap Typeahead with your CakePHP 2.0 application. We will avoid using helpers or plugins and stick with plain Javascript + jQuery. Make sure you have include jQuery, Bootstrap CSS and Bootstrap Javascript files in your CakePHP application. You can simply do it inside your default.ctp file ( the files are bootstrap.min.js and bootstrap.min.css ).

After that we will create controller, action and view to put our input box. In this tutorial I'll use my Cbunny application and Users controller. I'll start by creating typeahead action, here is the code :

``` php    
public function typeahead() {
    $this->User->recursive = 0;
    $this->set('users', $this->paginate());       
}
```


Nothing special happening rather than get current users from the table and paginate them. And here is the view :

``` html    
<div class="row">
    <div class="span12">

    <!-- Typeahead Auto Complete -->
    <div class="pull-right">
        <input type="text" data-provide="typeahead" id="user-typeahead">
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


On line 5-7, I am defining input text with typeahead attribute and ID that we will use in Javascript code. The next step is to create Javascript object in your layout file. So add this code snippet in your default.ctp file :

``` php    
$cbunny = array(
    'APP_PATH' => Router::url('/',true)
);
echo $this->Html->scriptBlock('var CbunnyObj = ' . $this->Javascript->object($cbunny) . ';');
```


You can change the $cbunny and CBunnyObj variable name to resemble your app name. However, the rest of the code has to be same as above. This snippet of code will create Javascript object which contains the root URL path of CakePHP.

After we have the Javascript object variable, let's continue by creating the Javascript code. Inside your application Javascript file add these code :

``` javascript    
$('#user-typeahead').typeahead({
  source: function (query, process) {
    return $.ajax({
      url: CbunnyObj.APP_PATH + 'users/typeahead_search',
      type: 'get',
      data: {q: query},
      dataType: 'json',
      success: function (json) {
        return process(json);
      }
    });
  }
});
```


In this code, we initialize the typeahead library and create AJAX request to the typeahead_search action. In the next step, we will create typeahead_search action that will handle AJAX request and return JSON result. Back to our users controller, create the typeahead action which will contain this code :

``` php    
public function typeahead_search() {
    $this->autoRender = false;
    $this->RequestHandler->respondAs('json');

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
        array_push($result, $user['User']['username']);
    }
    $users = $result;

    echo json_encode($users);
}
```

This action will receive the request, search the database for relevant result and return it on JSON format.
