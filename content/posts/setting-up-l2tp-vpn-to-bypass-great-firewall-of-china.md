+++
title = "Setting Up L2TP VPN to Bypass Great Firewall Of China"
date = "2017-01-11"
slug = "2017/01/11/setting-up-l2tp-vpn-to-bypass-great-firewall-of-china"
Categories = ["Unix and Linux", "L2TP"]
+++

Last month, I traveled to China for the second time. Unlike my first trip, this time I am more prepared to bypass the great firewall of China.

During my first trip in China, I was mainly relying on simple SSH tunnel to get access to Gmail and all other blocked services. This solution is unrealiable because I couldn't use it on my Android phone. Aside from that, I also kept having constant dropouts which explained in this blog post [http://blog.zorinaq.com/my-experience-with-the-great-firewall-of-china/](http://blog.zorinaq.com/my-experience-with-the-great-firewall-of-china/)

After an extensive research and also a recommendation from one of my friends, I decided to install an L2TP VPN server in Japan. I choose Japan because it's close to China and I can use Tokyo AWS Region.

I ended up using this ansible playbook that I found when I was looking for tutorials [https://github.com/jlund/streisand](https://github.com/jlund/streisand). It's basically an Ansible Playbook which help you to install various software such as OpenVPN, L2TP, Tor, etc. You just need to run one shell script and it will install all of those software to your target host.

### Running the playbook

Since I already have ansible installed, I just need to clone the project and run the setup script. If not a complete tutorial on how to get started you can check this installation guide here [https://github.com/jlund/streisand#installation](https://github.com/jlund/streisand#installation).

Cloning the project

```
git clone https://github.com/jlund/streisand.git && cd streisand
```

Running the setup script

```
./streisand
```

When you run the setup script, it will ask few questions such as where to host the server, AWS Access Keys, etc. I am using AWS because I can use the free tier to run the VPN server. On AWS, it will take around 45 minutes to finish the whole installation process.

### Using the VPN

When the whole installation finished, the playbook will create instructions files in the server. You need to SSH to the server in order to view the instruction.

```
ssh ubuntu@server-ip
```

Go to the NGINX folder to see file

```
cd /var/www/streisand/l2tp-ipsec
```

Read the instruction

```
cat index.md | more
```

In the file, you will find instructions on how to connect to the L2TP server from all different operating systems.
