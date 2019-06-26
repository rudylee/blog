---
title: "Migrate to Hugo From Octopress"
date: 2019-06-23T17:23:22+10:00
slug: "2019/06/23/migrate-to-hugo-from-octopress"
Categories: ["Go", "Hugo"]
---

Two weeks ago I decided to migrate my blog from Octopress to Hugo. I have been using Octopress as my blog engine since 2013 and I don't have any problems with it. I can easily generate my blog as a static site with Octopress and host it on Github. It is a lot better setup than using Wordpress which requires database and PHP server. However, Octopress is not actively developed anymore and this is one of the reasons why I decided to migrate my blog to Hugo. 

### The theme

The first thing I did before migrating my blog to Hugo is choosing the theme. Hugo provides a website where you can easily browse all available themes: [https://themes.gohugo.io/](https://themes.gohugo.io/). I ended up with [hyde-hyde](https://themes.gohugo.io/hyde-hyde/) theme which is a port from Hyde theme on Jekyll. I like the simplicity of the theme and I feel the theme is really suitable for a blog.

### Migrate the posts using Octohug

I was using [Octohug](https://github.com/rudylee/octohug) to migrate all my blog posts from Octopress from Hugo. I had to change a few things in original script to support my Octopress posts. Aside from that, it is a pretty straight forward process. You just need to clone + build the project, run it in your Octopress folder and copy the generated files to your Hugo folder.

### Images

I have a few images in my Octopress blog that I use in the posts. Moving these images are pretty easy. I just need to put the folders inside `static` folder in Hugo.

### Set permalinks

In my Octopress blog, I am using `https://blog.rudylee.com/:year/:month/:day/:title` as the permalink format. Hugo uses the same format except it will add `posts` between the domain name and `year`. The URL will end up something like this if I use the default setting `https://blog.rudylee.com/posts/:year/:month/:day/:title`.

### Change the blog from subdomain to subdirectory

As part of the migration, I also changed my blog URL from https://blog.rudylee.com to https://www.rudylee.com/blog. This is an optimal way to set up a blog because search engine will treat your blog as part of your domain instead of a separate website.

For this step, I set up a Cloudflare page rule that do 301 redirect from my subdomain to the subpage.

### Migrate Disqus

I am using [Disqus](https://disqus.com/) as my commenting system and I need to migrate Disqus because I changed my blog URL from subdomain to subpage. Fortunately, Disqus provides a few migration tools to help with this. 

I ended up using the CSV export and import tool to migrate all my comments.

### Conclusion

Overall the migration process went well. The most time consuming part is probably choosing the theme and configure it. Please check my Github repository if you want to see my blog configuration [https://github.com/rudylee/blog](https://github.com/rudylee/blog)

