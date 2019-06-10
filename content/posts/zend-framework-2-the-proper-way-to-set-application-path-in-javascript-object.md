+++
date = "2013-05-06"
slug = "2013/05/06/zend-framework-2-the-proper-way-to-set-application-path-in-javascript-object"
title = "'Zend Framework 2 : The proper way to set application path in Javascript Object'"
Categories = ["Zend Framework 2"]
Tags = ["ajax", "application path", "array", "basepath", "CakePHP", "cdata", "long time", "lt", "script type", "text javascript", "website register", "zend framework"]
+++

Storing application path inside Javascript object is a way to avoid "hard coded" URL inside your Javascript file.  It is pretty common to have like this in your Javascript file :

``` javascript    
    $.ajax({
        type: POST,
        url: 'http://localhost/my-website/register',
        data: dataJSON
    })
```


That approach is completely fine. However, when you need to deploy your application, you need to manually change all the URL to match with your server. The solution that I have been using for quite a long time is setting up Javascript object that contains path to my application.

In CakePHP, this can be easily done by using URL method inside Router Class. Here is the sample :

``` php  
$cbunny = array(
    'APP_PATH' => Router::url('/',true)
);
echo $this->Html->scriptBlock('var CbunnyObj = ' . $this->Javascript->object($cbunny) . ';');
```


In Zend Framework 2, you have to rely on serverUrl and basePath to achieve the same thing. Here is the proper way to do it in Zend Framework 2 :

``` javascript  
<script type="text/javascript">
    //<![CDATA[
        var CMSObj = {
            "APP_PATH":"<?php echo $this->serverUrl() . $this->basePath() ?>/"
        };
    //]]>
</script>
```



