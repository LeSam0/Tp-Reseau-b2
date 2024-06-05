# TP4 : Hardening Script

# I. Setup initial

🌞 **Setup `web.tp5.b2`**

```bash!
[mew@web ~]$ sudo dnf install nginx
Complete!
[mew@web ~]$ cat /var/www/app_nulle/index.html
<h1>Hello</h1>
[mew@web ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: cockpit dhcpv6-client ssh
  ports: 22/tcp 80/tcp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

🌞 **Setup `rp.tp5.b2`**


```bash!
[mew@rp ~]$ sudo dnf install nginx
Complete!
[mew@rp ~]$ cat /etc/nginx/conf.d/nginx.conf
server {
    listen    80;
    server_name   app.tp5.b2;

    location / {
        proxy_pass http://10.5.1.12;
    }
}
[mew@rp ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: cockpit dhcpv6-client ssh
  ports: 22/tcp 80/tcp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
[mew@rp ~]$ sudo systemctl status nginx
● nginx.service - The nginx HTTP and reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; disabled; preset: disabled)
     Active: active (running) since Thu 2024-01-25 16:04:19 CET; 23s ago
    Process: 12362 ExecStartPre=/usr/bin/rm -f /run/nginx.pid (code=exited, status=0/S>
    Process: 12363 ExecStartPre=/usr/sbin/nginx -t (code=exited, status=0/SUCCESS)
    Process: 12364 ExecStart=/usr/sbin/nginx (code=exited, status=0/SUCCESS)
   Main PID: 12365 (nginx)
      Tasks: 2 (limit: 11039)
     Memory: 2.0M
        CPU: 22ms
     CGroup: /system.slice/nginx.service
             ├─12365 "nginx: master process /usr/sbin/nginx"
             └─12366 "nginx: worker process"
```

🌞 **HTTPS `rp.tp5.b2`**

```bash
openssl req -new -newkey rsa:1024 -days 365 -nodes -x509 -keyout server.key -out server.crt
```

# II. Hardening script

[Script](./Ressource/script.txt)