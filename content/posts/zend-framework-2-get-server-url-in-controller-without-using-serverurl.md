+++
date = "2013-02-15"
slug = "2013/02/15/zend-framework-2-get-server-url-in-controller-without-using-serverurl"
title = "'Zend Framework 2 : get server URL in controller without using serverUrl()'"
Categories = ["Zend Framework 2"]
+++

Sometimes you need to be able to get current server URL inside controller in your Zend Framework 2 application. As you might know, you won't be able to use $this->serverUrl() method in the controller as it's a part of helper.

So, here is the code that I am using to get server URL in controller :

``` php    
    $server_url = $this->getRequest()->getUri()->getScheme() . '://' . $this->getRequest()->getUri()->getHost();
```

Probably it's not the best solution but it works for now. Please check the other solutions below:

## Other solutions from the comments below

``` php
    $helper = new Zend\View\Helper\ServerUrl();
    $url = $helper->__invoke(true);
```

``` php
    $this->getEvent()->getRouter()->assemble(array(), array('name'=>'home', 'force_canonical'=>true));
    // WHERE default is the name of your route, "default" or whatever you use
```

