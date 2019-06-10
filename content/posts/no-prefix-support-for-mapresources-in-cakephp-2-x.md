+++
date = "2012-11-28"
slug = "2012/11/28/no-prefix-support-for-mapresources-in-cakephp-2-x"
title = "No prefix support for mapResources in CakePHP 2.x"
Categories = ["CakePHP"]
+++

REST API is relatively easy to implement if you are using web framework to build your application. In Rails, you just need to add single 'resources'  entry in your routing file. In CakePHP, it has similar solution as you can read in the [Cookbook](http://book.cakephp.org/2.0/en/development/rest.html). However, currently there is no prefix support in CakePHP 2.x and this is confirmed in these links :



	
  * [http://cakephp.lighthouseapp.com/projects/42648/tickets/968-rest-routes-with-prefix](http://cakephp.lighthouseapp.com/projects/42648/tickets/968-rest-routes-with-prefix)

	
  * [https://github.com/cakephp/cakephp/pull/763](https://github.com/cakephp/cakephp/pull/763)


This is a drawback because you are most likely will use prefix to build REST API. In my case, I have products controller in my application which has default CRUD actions and another set of actions with prefix ( api_index, api_view, etc ). Those actions with prefix in front of it will act as our RESTful API.

You can try another approach by creating separate controller only to handle API request. For example, you will have to create controller called products_api to handle all restful API for specific controller. I am not a fan of this approach because you might end up having a lot of files and it's difficult to maintain.

So, if you are on the same boat as me, you can follow this solution that I found. This solution only requires you to add one line of code to Router.php file in CakePHP lib folder ( [https://github.com/DiegoMax/cakephp/commit/f203202ff78da930b472ecce817fdc6f19d6dfda](https://github.com/DiegoMax/cakephp/commit/f203202ff78da930b472ecce817fdc6f19d6dfda) ).

Not a best solution but I don't want to wait until CakePHP 3.x released to finish my first CakePHP + Backbone.JS app. That's all, have a nice day.
