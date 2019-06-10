+++
title = "How to Run Code Snippet in Heroku Rails Console"
date = "2018-08-18"
slug = "2018/08/18/how-to-run-code-snippet-in-heroku-rails-console"
Categories = ["Ruby on Rails", "Heroku"]
+++

Often in my day to day work, I need to run a snippet in rails console to fix or investigate issues. Since our application is hosted on Heroku, I can do this by running `heroku rails console --app app-name` and in a matter of seconds I am connected to the rails console on production.

In some cases, I need to run a really long code snippet especially if the fix needs to touch a lot of data. Usually I will copy the snippet line by line into the rails console because sometimes one of the lines will return a data and it will mess up the snippet.

After wasting a lot of time, I started thinking on a better way to do this. That's when I decided to use `eval` and `open` to help me running long code snippet. The idea is pretty simple, I need a place to securely host the code snippet, use `open` to read the code snippet and run it using `eval`.

At the moment, I am using Github secret gist. You can use S3 bucket or your own web server as long as heroku can access it. If you are using Github gist, make sure you use the `raw` link. You can grab the `raw` link by clicking the `Raw` button on the top right hand corner of your gist. The format of the link should be something like
`https://gist.githubusercontent.com/yourgithubaccount/randomhash/raw/randomhash/file.rb`

After you got the link, you can write 2 lines snippet to read and execute the file.

```ruby
file = open("put-link-to-your-code-snippet-here")
eval(file.read)
```

I hope you find that useful and let me know if you have a better way to do this.
