+++
title = "Monitor Background Jobs with New Relic Query Language"
date = "2017-07-01"
slug = "2017/07/01/monitor-background-jobs-with-new-relic-query-language"
Categories = ["New Relic"]
+++

# Background

In this blog post, I'll show you how to set up an alert to monitor your sidekiq jobs using New Relic Query Language and New Relic Alert.

I was given a task to find a solution to monitor our sidekiq jobs. In the past, I used New Relic Sidekiq Plugin ( https://newrelic.com/plugins/secondimpression/131 ) to do this.

The plugin is a Ruby app that connects to your Redis instance, retrieves all of the sidekiq metrics such as jobs, queues and send it to New Relic using the agent library.

This means you need to host the Ruby app somewhere and make sure the plugin can connect to your Redis instance.

However, I found a much better solution using NRQL that doesn't require you to set up a new server or install any plugins.

# New Relic Query Language ( NRQL )

NRQL definition from the official New Relic docs ( https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql )

The New Relic Query Language (NRQL), similar to SQL, is a query language for making calls against the Insights event database. NRQL enables you to query data collected from your application and transform that data into dynamic charts. From there, you can interpret your data to better understand how your application is used in a variety of ways.

Using NRQL, You can run a query to get the amount of background jobs that has been executed for a specific time period.

Here is the query to get the count of background jobs:

```
SELECT count(name) FROM Transaction WHERE transactionType='Other'
```

# New Relic Alert and NRQL

First thing you have to do is to create a New Relic alert policy using NRQL. See the screenshots below:

[![](/images/posts/nrql-sidekiq/1.png)](/images/posts/nrql-sidekiq/1.png)

[![](/images/posts/nrql-sidekiq/2.png)](/images/posts/nrql-sidekiq/2.png)

Choose `NRQL` on the `Categorize` step

[![](/images/posts/nrql-sidekiq/3.png)](/images/posts/nrql-sidekiq/3.png)

And put the the following query:

```
SELECT count(name) FROM Transaction WHERE transactionType='Other'
```

After that, you can set up a condition when it will fire the alert.

In the screenshot below, you can see that I set the alert to fire if there are no background jobs running within 15 minutes.

[![](/images/posts/nrql-sidekiq/4.png)](/images/posts/nrql-sidekiq/4.png)

[![](/images/posts/nrql-sidekiq/5.png)](/images/posts/nrql-sidekiq/5.png)

I hope this tutorial will give you an idea on how to monitor your background jobs.
