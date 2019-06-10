+++
title = "HAProxy and A/B Testing"
date = "2016-04-13"
slug = "2016/04/13/haproxy-and-a-slash-b-testing"
Categories = ["Unix and Linux"]
+++

Few weeks ago, I was given a task to create an A/B test using HAProxy. I need to make HAProxy to split traffic between two different applications ( Rails and NodeJS )

In this blog post, I'll explain how to achieve this.

### Create ACL for the page you want to A/B test

The first step you have to do is to create an ACL for the URL you want to A/B test. In this example, the URL path is `/ab-test-path`

```
acl ab_test_url path_beg /ab-test-path
```

### Direct the traffic based on ACL rule and cookie

```
# Send user to first backend if they have SITEID cookie with cookie_first_backend value
use_backend first-backend if { req.cook(SITEID) -m beg cookie_first_backend }

# Send user to second backend if they have SITEID cookie with cookie_second_backend value and the URL they request is ab_test_url
use_backend second-backend if { req.cook(SITEID) -m beg cookie_second_backend } ab_test_url

# If the doesn't have any cookie send them to ab-test backend
use_backend ab-test-backend if ab_test_url

# By default send all traffic to the first backend
default_backend first-backend
```

### Create all the backends

```
backend first-backend
        appsession JSESSIONID len 52 timeout 3h
        cookie SERVERID insert

        balance leastconn
        server  backend02a-aws-syd 10.0.105.102:80 check maxconn 3000 inter 30s
        server  backend02b-aws-syd 10.0.106.102:80 check maxconn 3000 inter 30s

backend second-backend
        server  backend03a-aws-syd 10.0.105.103:80 check maxconn 3000 inter 30s

backend ab-test-backend
        balance roundrobin
        cookie SITEID insert indirect nocache maxlife 48h

        server backend02a-aws-syd 10.0.105.102:80 weight 25 cookie cookie_first_backend
        server backend02b-aws-syd 10.0.106.102:80 weight 25 cookie cookie_first_backend

        server backend03a-aws-syd 10.0.105.103:80 weight 50 cookie cookie_second_backend
```

The final HAProxy config should be something like this:

```
listen  http 127.0.0.1:8080
        maxconn     18000

        # A/B Test ACLs
        acl ab_test_url path_beg /ab-test-path

        use_backend first-backend if { req.cook(SITEID) -m beg cookie_first_backend }
        use_backend second-backend if { req.cook(SITEID) -m beg cookie_second_backend } ab_test_url
        use_backend ab-test-backend if ab_test_url

        default_backend first-backend

backend first-backend
        appsession JSESSIONID len 52 timeout 3h
        cookie SERVERID insert

        balance leastconn
        server  backend02a-aws-syd 10.0.105.102:80 check maxconn 3000 inter 30s
        server  backend02b-aws-syd 10.0.106.102:80 check maxconn 3000 inter 30s

backend second-backend
        server  backend03a-aws-syd 10.0.105.103:80 check maxconn 3000 inter 30s

backend ab-test-backend
        balance roundrobin
        cookie SITEID insert indirect nocache maxlife 48h

        server backend02a-aws-syd 10.0.105.102:80 weight 25 cookie cookie_first_backend
        server backend02b-aws-syd 10.0.106.102:80 weight 25 cookie cookie_first_backend

        server backend03a-aws-syd 10.0.105.103:80 weight 50 cookie cookie_second_backend
```
