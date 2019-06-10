+++
title = "Sending email from Amazon EC2 using postfix and Amazon SES"
date = "2013-07-26"
slug = "2013/07/26/sending-email-from-amazon-ec2-using-postfix-and-amazon-ses"
Categories = ["Linux"]
+++

Sending email is a basic functionality that most of the applications need to support. In my company latest project, we have to send invitation emails to users through an Amazon EC2 instance. It is relatively easy task because I can use built in email library from Code Igniter and point it to Amazon SES. It works perfectly until my colleague realize that there is a slightly delay when the application sends the email.

It turns out that the built in email library inside Code Igniter has to wait for the response from Amazon SES to send the email. After a little bit of research, we found that we can solve the problem by using either sendmail or postfix to send the emails.  

## Sendmail

The first approach that we tried was using sendmail to send the email. You can find the tutorial to set it up in the [official Amazon SES documentation](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sendmail.html). It is pretty easy to set up because the default Amazon EC2 Linux Image already have sendmail installed by default. 

The problem that we found with this solution is you can only send email to verified email address only. The tutorial mentions that you need to request for production access to be able to send email to unverified email addresses.

## Postfix

After the sendmail approach, we decided to try the other approach which is using postfix to send the email. This is also easy to set up by following the tutorial from [official documentation](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/postfix.html). The only thing that is missing from the tutorial is to switch the MTA from sendmail to postfix. 

First thing that you have to do is to install postfix. This can be easily done through yum package manager :

``` bash
yum install postfix
```

You don't need to uninstall sendmail because they can just work together just fine. You just need to turn off the sendmail server and switch on postfix server.

``` bash
sudo /etc/init.d/sendmail stop
sudo /etc/init.d/postfix start
```

After that you need to switch the MTA from sendmail to postfix using this command

``` bash
sudo alternatives --set mta /usr/sbin/sendmail.postfix
```

If you get to this point, you just need to follow the tutorial from official documentation to set up postfix and use Amazon SES as the relay. After you are done with the configuration there is another thing that you need to solve. You might notice there is a timeout when you are trying to send emails in huge volume. The workaround for this problem is you have to ask Amazon to remove the limitation on your account.

Amazon put throttle on port 25 to prevent user to use Amazon EC2 for spam machine. This cause connection timeout which prevent you from sending email in real time. To solve this you have to send support request to remove this limitation. So, good luck with that.

