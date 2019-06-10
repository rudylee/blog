+++
title = "Google Spreadsheet as JSON API"
date = "2017-12-25"
slug = "2017/12/25/google-spreadsheet-as-json-api"
Categories = ["Google Spreadsheet"]
+++

Data store is an important piece in most of the modern applications. The implementation can range from a simple text file to a complicated database systems. In this blog post, I will show you how to use Google Spreadsheet as a data store for your application. 

Google Spreadsheet provides a convenient way to store, edit, share and retrieve data. This makes Google Spreadsheet appealing if you want to quickly prototype an app and don't want to spend time building a CRUD interface to manage your data. It is also allow you to output the spreadsheet data in JSON format. This means you use Google spreadsheet as your JSON API.

# Publish the spreadsheet to the web

In order to enable this feature, first you need to publish the spreadsheet to the web. You can easily do this by going to the File menu and choose Publish to the web. This only works if you own or have admin access to the spreadsheet. See the screenshot below.

[![](/images/posts/google-spreadsheet-json-api/publish-to-the-web.png)](/images/posts/google-spreadsheet-json-api/publish-to-the-web.png)

# Get the ID of the spreadsheet

The next thing that you have to do is getting the spreadsheet ID from the URL.

The URL of your spreadsheet should be something like this `https://docs.google.com/spreadsheets/d/17CAMo4mY7pdlk7jgV2385FLVzDV3L8cUDidhfge8U_J4/edit#gid=0`

The spreadsheet ID is the characters between the `d` and `edit`, which in the example above is `17CAMo4mY7pdlk7jgV2385FLVzDV3L8cUDidhfge8U_J4`

# Copy the ID and construct the JSON API endpoint

After retrieving the ID, you can start constructing the JSON API endpoint. The URL format as follow:

```
https://spreadsheets.google.com/feeds/list/replace-this-with-your-spreadsheet-id/od6/public/values?alt=json
```

If we are using the spreadsheet URL in the previous section ( https://docs.google.com/spreadsheets/d/17CAMo4mY7pdlk7jgVRmgD5FLVzDV3L8cUDiHaT8U_J4/edit#gid=0 ), the JSON API URL will be:

```
https://spreadsheets.google.com/feeds/list/17CAMo4mY7pdlk7jgVRmgD5FLVzDV3L8cUDiHaT8U_J4/od6/public/values?alt=json
```

# The spreadsheet is public but not published to the web

In some cases, you might want to use a public Google spreadsheet but it is not published to the web. I discovered from the official Google forum that you can use `importrange` formula to retrieve the data from another spreadsheet and import it into your spreadsheet.

```
=importrange("URL-TO-SPREADSHEET", "SHEET NAME!CELL RANGE")
```

Take for example this public spreadsheet that I don't have admin access to: `https://docs.google.com/spreadsheets/d/1ql32s8kcUB-Q8AEwxrCzPYJzNgaQ2CknW4J0rlnJqfE/edit#gid=1671204426`

I will create another spreadsheet and use the `importrange` formula to import the data from that public spreadsheet into my spreadsheet

```
=importrange("https://docs.google.com/spreadsheets/d/1ql32s8kcUB-Q8AEwxrCzPYJzNgaQ2CknW4J0rlnJqfE","SBW Optimal Conversions!A1:I190")
```

It should look something like this:

[![](/images/posts/google-spreadsheet-json-api/import-range.png)](/images/posts/google-spreadsheet-json-api/import-range.png)

As you might think, this solution is prone to error because the formula will break if the owner of the original spreadsheet changes the sheet's name.

It's something I can live with since it's so much easier to update the sheet's name rather than asking the owner to publish spreadsheet to the web.
