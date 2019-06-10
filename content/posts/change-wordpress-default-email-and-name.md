+++
date = "2011-06-20"
slug = "2011/06/20/change-wordpress-default-email-and-name"
title = "Change wordpress default email and name"
Categories = ["Wordpress"]
+++

Actually you can find this solution easily in Google. However, I'll put it in my blog just because I am lazy to find it again.

So wordpress has default email address and name which are "Wordpress" as the name, wordpress@yourdomain.com as the email. To change it you can use plugin or put these wordpress action to your functions.php file in themes folder :

    
``` php    
add_filter('wp_mail_from', 'new_mail_from');
add_filter('wp_mail_from_name', 'new_mail_from_name');

function new_mail_from($old) {
    return 'no-reply@rudylee.com';
}

function new_mail_from_name($old) {
    return 'Rudy';
}
```

Just change the email address and name to your's. Hope it works, cheers.
