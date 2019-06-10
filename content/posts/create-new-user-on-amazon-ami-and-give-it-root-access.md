+++
title = "Create new user on Amazon AMI and give it root access"
date = "2016-03-09"
slug = "2016/03/09/create-new-user-on-amazon-ami-and-give-it-root-access"
Categories = ["AWS", "Linux"]
+++

Setup your new EC2 instance on AWS and choose Amazon AMI.

SSH to your instance using your private key
```
ssh -i <path-to-your-pem-file> ec2-user@<ec2-endpoint-or-ip>
```

Change to root
```
sudo su
```

Create new group for your user ( in this case my group name is 'dev' )

```
groupadd dev
```

Create new user and assign it to your recently created group

```
useradd -g dev dev
```

Give the username root access
```
visudo
```

Add this to the bottom of the file
```
dev     ALL=(ALL)       NOPASSWD:ALL
```

Delete the password for 'dev' user
```
sudo passwd dev -d
```

Change to the 'dev' user
```
su dev
```

Try run sudo su whether you can gain root privileges
```
sudo su
```

Change user back to dev and set authorized_keys for ssh
```
exit
mkdir ~/.ssh
vi ~/.ssh/authorized_keys
chmod -R 700 ~/.ssh
```

If everything is correct, you should be able to change to root user from dev without providing any password.
