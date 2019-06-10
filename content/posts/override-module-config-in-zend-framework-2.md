+++
date = "2013-05-16"
slug = "2013/05/16/override-module-config-in-zend-framework-2"
title = "Override module config in Zend Framework 2"
Categories = ["Zend Framework 2"]
Tags = ["access password", "alphanumeric", "api access", "array", "config", "deployment", "heaps", "maintenance nightmare", "numerical characters", "rudy", "staging", "zend framework"]
+++

There is a time when you want to override module config in your Zend Framework 2 application. In my case, I have different configuration for SMS gateway in staging and live server. You can do this by overwriting the module.config.php file inside the module config's folder. However, there are heaps of configuration inside module.config.php file. This approach will lead to maintenance nightmare when you need to change one or more configuration inside the file.

The cleanest approach is to override specific configuration key by creating module-name.local.php file inside config/autoload folder. For example, you have "Admin" module and here is the sample module.config.php file :

``` php
return array(
    'sms' => array(
        'username' => 'rudy', //API access username
        'password' => 'rudy', //API access password
        'sender' => 'Rudy', // max of 11 alphanumeric or max of 15 numerical characters
    ),
);
```


You can override only the username by creating admin.local.php file inside config/autoload folder and put this code inside it :

``` php    
return array(
    'sms' => array(
        'username' => 'override', //API access username
    ),
);
```


Zend Framework 2 will read this file and overwrite the username key inside module.config.php. Now you can create script during your deployment process to create this file automatically.
