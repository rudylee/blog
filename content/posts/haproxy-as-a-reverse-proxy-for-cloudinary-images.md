+++
title = "HAProxy as a reverse proxy for cloudinary images"
date = "2016-12-05"
slug = "2016/12/05/haproxy-as-a-reverse-proxy-for-cloudinary-images"
Categories = ["HAProxy", "Unix and Linux"]
+++

We are using in one of our applications [Cloudinary](http://cloudinary.com/) to host and resize images on the fly. We are also using [Cloudflare](http://www.cloudflare.com) for our CDN and DNS management.

I was given a task to setup a CNAME subdomain in CloudFlare to forward the request to Cloudinary. This way we can still have the benefit of serving static images from CDN as well as reducing the Cloudinary bandwidth usage.

My solution is to set HAProxy as a reverse proxy which responsible to fetch images from Cloudinary server. You can see the overview diagram below:

[![](/images/posts/HAProxy-as-a-reverse-proxy.png)](/images/posts/HAProxy-as-a-reverse-proxy.png)

The first thing we have to do is to create an ACL in HAProxy for our cloudinary subdomain

In the configuration below, we are telling HAProxy to forward all requests from `cloudinary-asset.rudylee.com` to `cloudinary-backend`:

```
listen  http
        bind 127.0.0.1:8080
        maxconn     18000

        acl host_cloudinary hdr(host) -i cloudinary-asset.rudylee.com

        use_backend cloudinary-backend if host_cloudinary
```


Next one is to create a new backend.

```
backend cloudinary-backend
        http-request set-header Host res.cloudinary.com
        server cloudinary res.cloudinary.com:80
```

Restart HAProxy and you should be able to use the subdomain to serve images from Cloudinary (eg: http://cloudinary-asset.rudylee.com/rudylee/image/upload/12298848/icon/12379593943923.png )

Requesting the images through SSL should work if you have SSL termination configured in your HAProxy.
