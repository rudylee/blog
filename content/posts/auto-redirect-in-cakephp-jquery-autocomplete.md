+++
date = "2011-12-12"
slug = "2011/12/12/auto-redirect-in-cakephp-jquery-autocomplete"
title = "'Auto redirect in CakePHP jQuery AutoComplete '"
Categories = ["CakePHP"]
Tags = ["ajax autocomplete", "apps", "array", "array controller", "CakePHP", "demo", "guest id", "guest search", "jquery", "line 1", "line 3", "little bit", "result line", "search field", "select option", "time user"]
+++

> 

> 
> ## Demo : [http://cbunny.rudylee.com/autocomplete_redirect](http://cbunny.rudylee.com/autocomplete_redirect)
> 
> 
Demo source code :[ https://github.com/rudylee/cbunny]( https://github.com/rudylee/cbunny)


In my previous post ( [http://blog.rudylee.com/2011/07/25/jquery-ui-autocomplete-in-cakephp/](http://blog.rudylee.com/2011/07/25/jquery-ui-autocomplete-in-cakephp/) ) we have successfully integrated the jQuery AutoComplete with CakePHP with a little bit hacky way. Now we gonna add another feature that can redirect user to our desired place when they click the result value in the AutoComplete ( try the demo for more details ).

So let's start the coding ( I assume you have integrated the jQuery UI AutoComplete in your apps, if you haven't, just read my previous post ), so basically what we need to do are divided into 4 steps:



	
  * Wrap the jQuery UI AutoComplete search field in a form tag.

	
  * Add a hidden field which will hold the ID of the result.

	
  * Add 'select' option into the helper.

	
  * Set up the action that will handle the form submit


Here is the sample of the action code:


``` php
function admin_autoComplete() {
	if (!empty($this->data)) {
	    $this->redirect(array(
      'controller' => 'users',
      'action' => 'view', $this->data['Guest']['id']
        ));
    }
    $this->autoRender = false;
    $guests = $this->User->getGuests(array(
	    'conditions' => array(
		'OR' => array(
		    'User.name LIKE' => '%' . $_GET['term'] . '%',
		    'User.surname LIKE' => '%' . $_GET['term'] . '%'
		)
	    )
		));
    echo json_encode($this->User->autoComplete_encode($guests));
  }
```
Just ignore line 8 and so, we gonna focus on line 2 to 7. In that line, I redirect the user to the view action which based on the Guest ID which I got from the form. You can change the controller/action in this section. I hope everything are clear. Cheers.
