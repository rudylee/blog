+++
title = "Run Sidekiq Jobs Without Starting Worker Process"
date = "2017-08-06"
slug = "2017/08/06/run-sidekiq-jobs-without-starting-worker-process"
Categories = ["Ruby on Rails"]
+++

You can add the code snippet below to `config/initializers/sidekiq.rb` if you don't want to start a separate sidekiq workers.

The configuration below will make sure that the sidekiq jobs will be executed without worker process.

This is handy if you don't want to open an extra terminal tab or tmux window for worker process.

```ruby
# config/initializers/sidekiq.rb
if Rails.env.development?
  require 'sidekiq/testing'
  Sidekiq::Testing.inline!
end
```

See the official Sidekiq wiki for more information: https://github.com/mperham/sidekiq/wiki/Testing
