+++
date = "2012-02-12"
slug = "2012/02/12/rails-set-up-namespace-and-redirect-from-namespace"
title = "Rails set up namespace and redirect from namespace"
Categories = ["Ruby on Rails"]
Tags = ["admin users", "CakePHP", "class admin", "controller name", "directory browser", "folders", "left hand side", "new folder", "prefixes", "products resources", "screenshot", "sessions", "users actions"]
+++

In order to differentiate between admin actions and users actions, you can set up what called "namespace" in your rails apps. The basic idea of this feature is you will have different controller and view files for each role in your application.

This concept is similar with prefixes in CakePHP. However,  CakePHP allows you to put different action in one controller file, while in rails you have to create different controller and view file for the new namespace. Here is the sample namespace code that I put in my routes.rb file :

``` ruby
namespace :admin do
  resources :users
  resources :products
  resources :categories
end
```


The code means that users, products and categories will have admin namespace. The next step is to create new folder in your controller and view folder called "admin". Here is the screenshot ( see the directory browser on the left hand side ) :

[![](http://blog.rudylee.com/wp-content/uploads/2012/04/routes-rb.png)](http://blog.rudylee.com/wp-content/uploads/2012/04/routes-rb.png)

Put the template and controller files inside these folders. You have to add Admin:: in front of the class definition of your controller file. So it's gonna be like this :

``` ruby    
    class Admin::UsersController < ApplicationController
```


After you set up everything done, you can try to access your apps through http://your-url/admin/controller-path ( ex: http://localhost:3000/admin/users ). It should automatically pick the controller and view files from admin folder. And if you want to redirect to the original route, you have to add '/' in front of the controller name. Here is the code :

``` ruby    
    redirect_to :controller => "/sessions",:action => "new"
```

It means you will redirect the user to session controller outside of the namespace and load "new" action. That's all.
