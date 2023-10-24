# Tp 2 Linux


## *I. Topologie réseau*

**️Compte-rendu : (Sur node1.lan1.tp2)**

afficher ses cartes réseau et sa table de routage

```
[Mew@node1 ~]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:24:13:e7 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe24:13e7/64 scope link
       valid_lft forever preferred_lft forever
       
[Mew@node1 ~]# ip route show
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s8 proto static metric 100
```

prouvez qu'il peut joindre node2.lan2.tp2

```
[Mew@node1 ~]# ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=0.438 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=0.413 ms
64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=0.420 ms
^C
--- 10.1.2.12 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2032ms
rtt min/avg/max/mdev = 0.413/0.423/0.438/0.010 ms
```

prouvez avec un traceroute que le paquet passe bien par router.tp2

```
[Mew@node1 ~]# traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  0.502 ms  0.514 ms  0.538 ms
 2  10.1.2.12 (10.1.2.12)  0.511 ms !X  0.501 ms !X  0.467 ms !X
```

## *II. Interlude accès internet*

**️Sur router.tp2 :**

prouvez que vous avez un accès internet (ping d'une IP publique)
prouvez que vous pouvez résoudre des noms publics (ping d'un nom de domaine public)

```
[Mew@router ~]# ping ynov.com
PING ynov.com (104.26.10.233) 56(84) bytes of data.
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=1 ttl=56 time=10.7 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=2 ttl=56 time=10.6 ms
^C
--- ynov.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 10.646/10.680/10.715/0.034 ms

[Mew@router ~]# ping 104.26.10.233
PING 104.26.10.233 (104.26.10.233) 56(84) bytes of data.
64 bytes from 104.26.10.233: icmp_seq=1 ttl=56 time=12.7 ms
64 bytes from 104.26.10.233: icmp_seq=2 ttl=56 time=11.4 ms
^C
--- 104.26.10.233 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 11.355/12.022/12.690/0.667 ms
```

**️️Accès internet LAN1 et LAN2 :**

ajoutez une route par défaut sur les deux machines du LAN1 et les deux machines du LAN2

```
[Mew@node1 ~]# sudo ip route add default via 10.1.1.254 dev enp0s8
[Mew@node1 ~]# sudo ip route add default via 10.1.1.254 dev enp0s8
[Mew@node2 ~]# sudo ip route add default via 10.1.2.254 dev enp0s8
[Mew@node2 ~]# sudo ip route add default via 10.1.2.254 dev enp0s8
```

configurez l'adresse d'un serveur DNS que vos machines peuvent utiliser pour résoudre des noms

```
[Mew@node1 ~]# sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s8

'DNS1=1.1.1.1'

[Mew@node1 ~]# sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s8

'DNS1=1.1.1.1'

[Mew@node2 ~]# sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s8

'DNS1=1.1.1.1'

[Mew@node2 ~]# sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s8

'DNS1=1.1.1.1'

```

dans le compte-rendu, mettez-moi que la conf des points précédents sur node2.lan1.tp2

```
[Mew@node2 ~]# cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.12
NETMASK=255.255.255.0

DNS1=1.1.1.1

[Mew@node2 ~]# ip r s
default via 10.1.1.254 dev enp0s8
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.12 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s8 proto static metric 100
```

prouvez que node2.lan1.tp2 a un accès internet :

il peut ping une IP publique
il peut ping un nom de domaine public

```
[Mew@node1 ~]# ping ynov.com
PING ynov.com (104.26.10.233) 56(84) bytes of data.
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=1 ttl=55 time=10.3 ms
^C
--- ynov.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 10.265/10.265/10.265/0.000 ms
[Mew@node1 ~]# ping 104.26.10.233
PING 104.26.10.233 (104.26.10.233) 56(84) bytes of data.
64 bytes from 104.26.10.233: icmp_seq=1 ttl=55 time=10.9 ms
64 bytes from 104.26.10.233: icmp_seq=2 ttl=55 time=10.9 ms
^C
--- 104.26.10.233 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 10.893/10.898/10.904/0.005 ms
```

## *III. Services réseau*

### *1. DHCP :*

**Sur dhcp.lan1.tp2**

n'oubliez pas de renommer la machine (node2.lan1.tp2 devient dhcp.lan1.tp2)

changez son adresse IP en 10.1.1.253

```
[Mew@dhcp ~]# cat /etc/hostname
dhcp.lan1.tp2

[Mew@dhcp ~]# cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.253
NETMASK=255.255.255.0

DNS1=1.1.1.1
```

setup du serveur DHCP:

-commande d'installation du paquet
-fichier de conf
-service actif

```
[Mew@dhcp ~]# sudo dnf install dhcp-server -y
Last metadata expiration check: 4:16:06 ago on Tue Oct 24 14:23:30 2023.
        128 k
[...]
Installed:
  dhcp-common-12:4.4.2-18.b1.el9.noarch      dhcp-server-12:4.4.2-18.b1.el9.x86_64

Complete!

[Mew@dhcp ~]# cat /etc/dhcp/dhcpd.conf
# create new
# specify domain name
option domain-name     "srv.world";
# specify DNS server's hostname or IP address
option domain-name-servers     dlp.srv.world;
# default lease time
default-lease-time 600;
# max lease time
max-lease-time 7200;
# this DHCP server to be declared valid
authoritative;
# specify network address and subnetmask
subnet 10.1.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP address
    range dynamic-bootp 10.1.1.100 10.1.1.200;
    # specify broadcast address
    option broadcast-address 10.0.0.255;
    # specify gateway
    option routers 10.1.1.254;
    option domain-name-servers 1.1.1.1;
}

[Mew@dhcp ~]# systemctl status dhcpd
● dhcpd.service - DHCPv4 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd.service; enabled; preset: disabled)
     Active: active (running) since Tue 2023-10-24 18:41:38 CEST; 3min 30s ago
       Docs: man:dhcpd(8)
             man:dhcpd.conf(5)
   Main PID: 1814 (dhcpd)
     Status: "Dispatching packets..."
      Tasks: 1 (limit: 11053)
     Memory: 5.2M
        CPU: 7ms

```


**Sur node1.lan1.tp2**

```
[Mew@node1 ~]# nmcli con down id 'enp0s8'

[Mew@node1 ~]# nmcli con up id 'enp0s8'

[Mew@node1 ~]# ip a
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:24:13:e7 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s8
       valid_lft 565sec preferred_lft 565sec
    inet6 fe80::a00:27ff:fe24:13e7/64 scope link
       valid_lft forever preferred_lft forever
       
[Mew@node1 ~]# ip r s
default via 10.1.1.254 dev enp0s8 proto dhcp src 

[Mew@node1 ~]# ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=0.509 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=0.579 ms
64 bytes from 10.1.2.11: icmp_seq=3 ttl=63 time=0.516 ms
^C
--- 10.1.2.11 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2085ms
rtt min/avg/max/mdev = 0.509/0.534/0.579/0.031 ms
```


### *2. Web web web :*

**Sur web.lan2.tp2**

n'oubliez pas de renommer la machine (node2.lan2.tp2 devient web.lan2.tp2)

```
[Mew@node2 ~]# cat /etc/hostname
web.lan2.tp2
```

setup du service Web

```
[Mew@web ~]# dnf install nginx
Last metadata expiration check: 1:58:20 ago on Tue Oct 24 17:01:57 2023.
[...]
Installed:
  nginx-1:1.20.1-14.el9_2.1.x86_64              nginx-core-1:1.20.1-14.el9_2.1.x86_64
  nginx-filesystem-1:1.20.1-14.el9_2.1.noarch   rocky-logos-httpd-90.14-1.el9.noarch

Complete!

[Mew@web ~]# sudo cat /var/www/site_nul/index.htlm
<html>
<body>
Test Nginx
TP2
</body>
</html>

[Mew@web ~]# sudo cat /etc/nginx/nginx.conf

    server {
        listen       80;
        listen       [::]:80;
        server_name  _;
        root         /var/html/site_nul;
        index index.html;

[Mew@web ~]# sudo systemctl status nginx
● nginx.service - The nginx HTTP and reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; disabled; preset: disabled)
     Active: active (running) since Tue 2023-10-24 19:17:31 CEST; 5s ago
    Process: 1498 ExecStartPre=/usr/bin/rm -f /run/nginx.pid (code=exited, status=0/SU>
    Process: 1499 ExecStartPre=/usr/sbin/nginx -t (code=exited, status=0/SUCCESS)
    Process: 1500 ExecStart=/usr/sbin/nginx (code=exited, status=0/SUCCESS)
   Main PID: 1501 (nginx)
      Tasks: 2 (limit: 11053)
     Memory: 1.9M
        CPU: 17ms
     CGroup: /system.slice/nginx.service
             ├─1501 "nginx: master process /usr/sbin/nginx"
             └─1502 "nginx: worker process"

[Mew@web ~]# sudo firewall-cmd --list-all
  ports: 22/tcp 80/tcp
```

prouvez qu'il y a un programme NGINX qui tourne derrière le port 80 de la machine

```
[Mew@web ~]# sudo ss -laputn | grep nginx
tcp   LISTEN 0      511          0.0.0.0:80        0.0.0.0:*     users:(("nginx",pid=1502,fd=6),("nginx",pid=1501,fd=6))
tcp   LISTEN 0      511             [::]:80           [::]:*     users:(("nginx",pid=1502,fd=7),("nginx",pid=1501,fd=7))
```

prouvez que le firewall est bien configuré

```
[Mew@web ~]# sudo firewall-cmd --list-all
  ports: 22/tcp 80/tcp
```


**Sur node1.lan1.tp2**

éditez le fichier hosts pour que site_nul.tp2 pointe vers l'IP de web.lan2.tp2

```

```

visitez le site nul avec une commande curl et en utilisant le nom site_nul.tp2

```
[Mew@node1 ~]# cat /etc/hosts
10.1.2.12 site_nul.tp2

[Mew@node1 ~]# curl site_nul.tp2
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
```
