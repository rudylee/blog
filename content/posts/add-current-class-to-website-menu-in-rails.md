+++
title = "Add 'current' class to website menu in Rails"
date = "2014-01-15"
slug = "2014/01/15/add-current-class-to-website-menu-in-rails"
Categories = ["Ruby on Rails"]
+++

It is common to have 'active' state or 'current' state on website navigation. This will help visitors to know which page they have selected.

This solution is based on Stackoverflow's question which I couldn't find. First, I'll create a method inside Rails application_helper.rb file. I'll call this method cp(). Here are the syntax:

``` ruby application_helper.rb
module ApplicationHelper
  def cp(path)
    current_route = Rails.application.routes.recognize_path(path)
    "current" if current_page?(path) or params[:controller] == current_route[:controller]
  end
end
```

The method uses current_page and Rails.application.routes.recognize_path to get information about current page.

After that we can use it in our view. Here is the example:

``` ruby application.html.erb
<nav id="menu-panel">
    <%= link_to 'SERVICES', services_path, class: cp('/services') %>
    <%= link_to 'FACILITIES', facilities_path, class: cp('/facilities') %>
    <%= link_to 'ABOUT', about_path, class: cp('/about') %>
    <%= link_to 'CAREERS', careers_path, class: cp(careers_path) %>
    <%= link_to 'BLOG', blog_index_path, class: cp(blog_index_path) %>
    <%= link_to 'CONTACT', contact_path, class: cp('/contact') %>
    <a href="#" id="close-menu-panel"><b>CLOSE</b></a>
</nav>
```

I hope that helps.
