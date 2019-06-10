+++
date = "2010-08-30"
slug = "2010/08/30/add-bridge-assign-unique-ip-for-each-container-in-openvz"
title = "Add bridge and assign unique IP for each container in OpenVZ"
Categories = ["Unix and Linux"]
Tags = ["bridge", "openvz", "venet", "veth"]
+++

I am writing this tutorial to refresh my mind ( I am not configuring the machine right now ), so forgive me if the explanations are not clear and structured.

After successfully installed the OpenVZ, you need to configure the IP for the containers. If you are using the built in "Venet" you will end up making the host as the gateway. In the other words if you traceroute to your container IP, it will going through your host then to your container. Here are the sample of the scenario :

1. Host IP : 202.58.181.2

2. Container 1 : 202.58.181.50

3. Container 2 : 202.58.181.51

Basically if you use the venet, if you traceroute to the Container 1 the result should be : Your ISP -> 202.58.181.2 -> 202.58.181.50 so the IP of the Host is showed up. Same if you try to traceroute to the second container. Thus, my solution to overcome this problem are :

1. Make a bridge using brctl command

2. Use the Veth instead of Venet

3. Put all the Veth into the bridge

4. Assign the Host IP to the bridge

If you are not ASSIGN the host IP to the bridge, you can't access the host machine. I followed the guidelines from this link [http://wiki.openvz.org/Using_veth_and_brctl_for_protecting_HN_and_saving_IP_addresses](http://wiki.openvz.org/Using_veth_and_brctl_for_protecting_HN_and_saving_IP_addresses)

Here is my /etc/rc.local configuration looks like :

``` bash
#!/bin/sh
#
# This script will be executed *after* all the other init scripts.
# You can put your own initialization stuff in here if you don't
# want to do the full Sys V style init stuff.

touch /var/lock/subsys/local
brctl addbr vzbr0
brctl addif vzbr0 eth0
brctl addif vzbr0 veth1.0
brctl addif vzbr0 veth2.0
brctl addif vzbr0 veth3.0
brctl addif vzbr0 veth4.0
ifconfig vzbr0 0
ip addr add 202.58.181.2/25 dev vzbr0
cd /usr/local/webvz/ && /usr/bin/ruby script/server &>/dev/null &
```

I'll update this post if I need to configure another VPS Server.
