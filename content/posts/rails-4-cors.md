+++
title = "Rails 4 CORS"
date = "2013-10-29"
slug = "2013/10/29/rails-4-cors"
Categories = ["Ruby on Rails"]
+++

## McFlyyy pointed out another solution to solve this problem. I haven't tested it myself so follow it at your own risk [Click Here](https://stackoverflow.com/questions/18538549/cant-get-rack-cors-working-in-rails-application/20464939#20464939)

I was trying to use Rails to build REST API for my AngularJS app and came across CORS error on my Chrome developer tools. 

According to [Alexey Vasiliev](http://leopard.in.ua/2012/07/08/using-cors-with-rails/), Cross-origin resource sharing (CORS) is a web browser technology specification which defines ways for a web server to allow its resources to be accessed by a web page from a different domain. Such access would otherwise be forbidden by the same origin policy. CORS defines a way in which the browser and the server can interact to determine whether or not to allow the cross-origin request. It is a compromise that allows greater flexibility, but is more secure than simply allowing all such requests. CORS is supported in the following browsers:

After following couple of outdated tutorials, I found the quick solution for it. Here are the steps:

# Add route to handle OPTIONS method

AngularJS using OPTIONS method to check the CORS support on the API server. Thus, you need to add line in your route file to handle this. This can be done by adding code like this 

``` ruby
match 'users', to: 'users#index', via: [:options]
resources :users
```

To check whether your configuration is correct you can run 'rake routes'. It should print out something like this:

``` bash
   Prefix Verb    URI Pattern               Controller#Action
    users OPTIONS /users(.:format)          users#index
          GET     /users(.:format)          users#index
          POST    /users(.:format)          users#create
 new_user GET     /users/new(.:format)      users#new
edit_user GET     /users/:id/edit(.:format) users#edit
     user GET     /users/:id(.:format)      users#show
          PATCH   /users/:id(.:format)      users#update
          PUT     /users/:id(.:format)      users#update
          DELETE  /users/:id(.:format)      users#destroy
     root GET     /                         users#index
```

You can see on the second line, we handle OPTIONS verb and redirect to index action.

# Add before_filter and after_filter to allow CORS

The next step is we need to return proper header to tell AngularJS that our server allow CORS. Here is the sample controller file:

``` ruby
UsersController < ApplicationController

  skip_before_filter :verify_authenticity_token
  before_filter :cors_preflight_check
  after_filter :cors_set_access_control_headers
  
  # For all responses in this controller, return the CORS access control headers.
  def cors_set_access_control_headers
    headers['Access-Control-Allow-Origin'] = '*'
    headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    headers['Access-Control-Max-Age'] = "1728000"
  end
 
  # If this is a preflight OPTIONS request, then short-circuit the
  # request, return only the necessary headers and return an empty
  # text/plain.

  def cors_preflight_check
    headers['Access-Control-Allow-Origin'] = '*'
    headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    headers['Access-Control-Allow-Headers'] = 'X-Requested-With, X-Prototype-Version'
    headers['Access-Control-Max-Age'] = '1728000'
  end

  def index
    @users = User.all

    respond_to do |format|
      format.json { render :json => @users }
    end
  end
end
```

We need to add skip_before_filter :verify_authenticity_token because Rails will return 422 status code and error message 'Can't verify CSRF token authenticity'
