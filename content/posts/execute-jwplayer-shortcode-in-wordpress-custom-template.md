+++
date = "2012-01-08"
slug = "2012/01/08/execute-jwplayer-shortcode-in-wordpress-custom-template"
title = "Execute JWPlayer shortcode in Wordpress custom template"
Categories = ["Wordpress"]
+++

JWPlayer has become my favorite video player for clients website especially after they release their [official Wordpress plugin](http://wordpress.org/extend/plugins/jw-player-plugin-for-wordpress/). The plugin almost done all the basic things ( shortcode, custom player, etc ). It's also integrated seamlessly with the Wordpress Media library which makes your life so much easier because you can easily add the player to a post straightly from media library. However, aside from all that simple integration and setup, it lacks of documentation could cause a headache especially if you are trying to do something out of the lane.

Today, I was trying to use JWPlayer plugin to show video in a custom post type template which grab the video file from external URL ( not from Media Library ). I was thinking this would be an easy task because I could easily execute the shortcode using do_shortcode() function in Wordpress. But, apparently JWPlayer plugin handle the shortcode quite different from another plugin so you have to use jwplayer_tag_callback() function instead of do_shortcode(). I don't know the reason why they make it like that but as long as it works then it's fine. Here is the sample code to make it clear:

    
``` php    
//won't work
do_shortcode("[jwplayer file='http://xxx.com/xxx.mp4']");

//obviously will work
jwplayer_tag_callback("[jwplayer file='http://xxx.com/xxx.mp4']");
```
    
