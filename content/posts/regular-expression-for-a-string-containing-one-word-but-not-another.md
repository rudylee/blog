+++
title = "Regular Expression For A String Containing One Word But Not Another"
date = "2017-07-28"
slug = "2017/07/28/regular-expression-for-a-string-containing-one-word-but-not-another"
Categories = ["Regex"]
+++

Last weekend, one our apps that is hosted on Heroku were reporting a lot of R14 errors.

R14 is an error that thrown by Heroku if the machine is running out of memory.

I quickly jumped into (logentries)[https://logentries.com/] to download the log file and opened it in Sublime Text.

However, I was having problem finding the request that is causing the problem because we also have our background job workers reporting R14 errors.

I decided to use regex to find a line that has `R14` but doesn't contain any of the background worker's name,

This is the regex that I used to find the line:

```
^(?!.*(lowworker|highworker|run)).*R14.*$
```

The regex above will match the line that has `R14` but doesn't contain `lowworker` or `highworker` and `run`
