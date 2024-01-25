# TP1 : Premiers pas Docker

# I. Init

## 1. Installation de Docker

## 2. Vérifier que Docker est bien là

## 3. sudo c pa bo

🌞 **Ajouter votre utilisateur au groupe `docker`**

```bash!
[mew@dock ~]$  sudo usermod -aG docker $USER
[mew@dock ~]$  newgrp docker
[mew@dock ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## 4. Un premier conteneur en vif

🌞 **Lancer un conteneur NGINX**

- avec la commande suivante :

```bash
docker run -d -p 9999:80 nginx
```

🌞 **Visitons**

- vérifier que le conteneur est actif avec une commande qui liste les conteneurs en cours de fonctionnement
```bash
[mew@dock ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
69b1b3026c17   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:9999->80/tcp, :::9999->80/tcp   cranky_pike
```
- afficher les logs du conteneur
```bash
[mew@dock ~]$ docker logs cranky_pike
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/12/22 11:31:23 [notice] 1#1: using the "epoll" event method
2023/12/22 11:31:23 [notice] 1#1: nginx/1.25.3
2023/12/22 11:31:23 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2023/12/22 11:31:23 [notice] 1#1: OS: Linux 5.14.0-362.13.1.el9_3.x86_64
2023/12/22 11:31:23 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1073741816:1073741816
2023/12/22 11:31:23 [notice] 1#1: start worker processes
2023/12/22 11:31:23 [notice] 1#1: start worker process 29
```
- afficher toutes les informations relatives au conteneur avec une commande `docker inspect`
```bash
[mew@dock ~]$ docker inspect cranky_pike
[
    {
        "Id": "69b1b3026c178d9a90c860f7f4842f6c8d6ce0b964df0ac1842e3d89e18360cc",
        "Created": "2023-12-22T11:31:22.989777716Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1749,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-22T11:31:23.647490751Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:d453dd892d9357f3559b967478ae9cbc417b52de66b53142f6c16c8a275486b9",
        "ResolvConfPath": "/var/lib/docker/containers/69b1b3026c178d9a90c860f7f4842f6c8d6ce0b964df0ac1842e3d89e18360cc/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/69b1b3026c178d9a90c860f7f4842f6c8d6ce0b964df0ac1842e3d89e18360cc/hostname",
        "HostsPath": "/var/lib/docker/containers/69b1b3026c178d9a90c860f7f4842f6c8d6ce0b964df0ac1842e3d89e18360cc/hosts",
        "LogPath": "/var/lib/docker/containers/69b1b3026c178d9a90c860f7f4842f6c8d6ce0b964df0ac1842e3d89e18360cc/69b1b3026c178d9a90c860f7f4842f6c8d6ce0b964df0ac1842e3d89e18360cc-json.log",
        "Name": "/cranky_pike",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "9999"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                44,
                87
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/c105101aa5d1b0c28ae080759eb643473ada063302470ecd24952c7b8e44d9fb-init/diff:/var/lib/docker/overlay2/1888c29c13b5ce27b57a06eb79704cbf9ac43826d8f0a4f2077de40a4cd80d18/diff:/var/lib/docker/overlay2/3ab4d9e549faa310ac6153e53ca288b113675c777873a4af8bbd976b88b2c4d6/diff:/var/lib/docker/overlay2/33efb64949ce2a7bf75776899ffdf726aca938a489c72d878fdb2776a233eaa1/diff:/var/lib/docker/overlay2/044b21484278fc7f1304f5165c8696f041beb8e77d0dd32d71de17e46899125a/diff:/var/lib/docker/overlay2/1641bff91396920a336211e6c9f5cf3606770cfe7247eda2ba902346802cf7d0/diff:/var/lib/docker/overlay2/cb56841a2632263ce52a28adb7680c1b539ab3479e837b4cd7e0a06ccbc6dc55/diff:/var/lib/docker/overlay2/cffbca002c88212905a0f4f8578d600e4991d96fb1c83acd6f737ad8646b6472/diff",
                "MergedDir": "/var/lib/docker/overlay2/c105101aa5d1b0c28ae080759eb643473ada063302470ecd24952c7b8e44d9fb/merged",
                "UpperDir": "/var/lib/docker/overlay2/c105101aa5d1b0c28ae080759eb643473ada063302470ecd24952c7b8e44d9fb/diff",
                "WorkDir": "/var/lib/docker/overlay2/c105101aa5d1b0c28ae080759eb643473ada063302470ecd24952c7b8e44d9fb/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "69b1b3026c17",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.3",
                "NJS_VERSION=0.8.2",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "3f78e597aada56d838f3909a1918d13e93fdd2c027e522d48576028df32956c6",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "9999"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "9999"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/3f78e597aada",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "dc42f87961dded30c24b26fcf31e5ae4fd97ecaf586e142500e282b2788d6f79",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "819e00b144644e00f9c667cd8529954ccec782a0e11fadf71bf4a13b403ed25d",
                    "EndpointID": "dc42f87961dded30c24b26fcf31e5ae4fd97ecaf586e142500e282b2788d6f79",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```
- afficher le port en écoute sur la VM avec un `sudo ss -lnpt`
```bash
[mew@dock ~]$ sudo ss -lnpt
State      Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
LISTEN     0          4096                 0.0.0.0:9999               0.0.0.0:*         users:(("docker-proxy",pid=1706,fd=4))
LISTEN     0          4096                    [::]:9999                  [::]:*         users:(("docker-proxy",pid=1711,fd=4))
```
- ouvrir le port `9999/tcp` (vu dans le `ss` au dessus normalement) dans le firewall de la VM
```bash
[mew@dock ~]$ sudo firewall-cmd --add-port=9999/tcp --permanent
success
[mew@dock ~]$ sudo firewall-cmd --reload
success
```
- depuis le navigateur de votre PC, visiter le site web sur `http://IP_VM:9999`
```bash
[mew@dock ~]$ curl http://10.7.1.10:9999
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

🌞 **On va ajouter un site Web au conteneur NGINX**

- créez un dossier `nginx`
  - pas n'importe où, c'est ta conf caca, c'est dans ton homedir donc `/home/<TON_USER>/nginx/`
- dedans, deux fichiers : `index.html` (un site nul) `site_nul.conf` (la conf NGINX de notre site nul)
- exemple de `index.html` :

```html
<h1>MEOOOW</h1>
```

- config NGINX minimale pour servir un nouveau site web dans `site_nul.conf` :

```nginx
server {
    listen        8080;

    location / {
        root /var/www/html;
    }
}
```

- lancez le conteneur avec la commande en dessous, notez que :


```bash
docker run -d -p 9999:8080 -v /home/<USER>/nginx/index.html:/var/www/html/index.html -v /home/<USER>/nginx/site_nul.conf:/etc/nginx/conf.d/site_nul.conf nginx
```

🌞 **Visitons**

- vérifier que le conteneur est actif
```bash!
[mew@dock ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                               NAMES
388e43c33cd2   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:9999->8080/tcp, :::9999->8080/tcp   infallible_gates
```
- aucun port firewall à ouvrir : on écoute toujours port 9999 sur la machine hôte (la VM)
- visiter le site web depuis votre PC
```bash!
[mew@dock ~]$ curl http://10.7.1.10:9999
<h1>MEOOOW</h1>
```

## 5. Un deuxième conteneur en vif

Cette fois on va lancer un conteneur Python, comme si on voulait tester une nouvelle lib Python par exemple. Mais sans installer ni Python ni la lib sur notre machine.

On va donc le lancer de façon interactive : on lance le conteneur, et on pop tout de suite un shell dedans pour faire joujou.

🌞 **Lance un conteneur Python, avec un shell**

```bash
docker run -it python bash
```

🌞 **Installe des libs Python**

```bash!
root@9dcd96fcba8d:/# pip install aiohttp
root@9dcd96fcba8d:/# pip install aioconsole
root@9dcd96fcba8d:/# python
Python 3.12.1 (main, Dec 19 2023, 20:14:15) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import aiohttp
>>>
```

# II. Images

## 1. Images publiques

🌞 **Récupérez des images**

```bash!
[mew@dock ~]$ docker pull python:3.11
3.11: Pulling from library/python
Status: Downloaded newer image for python:3.11
docker.io/library/python:3.11
[mew@dock ~]$ docker pull mysql:5.7
5.7: Pulling from library/mysql
Status: Downloaded newer image for mysql:5.7
docker.io/library/mysql:5.7
[mew@dock ~]$ docker pull wordpress:latest
latest: Pulling from library/wordpress
Status: Downloaded newer image for wordpress:latest
docker.io/library/wordpress:latest
[mew@dock ~]$ docker pull linuxserver/wikijs
Using default tag: latest
latest: Pulling from linuxserver/wikijs
Status: Downloaded newer image for linuxserver/wikijs:latest
docker.io/linuxserver/wikijs:latest
[mew@dock ~]$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
linuxserver/wikijs   latest    869729f6d3c5   7 days ago     441MB
mysql                5.7       5107333e08a8   9 days ago     501MB
python               latest    fc7a60e86bae   2 weeks ago    1.02GB
wordpress            latest    fd2f5a0c6fba   2 weeks ago    739MB
python               3.11      22140cbb3b0c   2 weeks ago    1.01GB
nginx                latest    d453dd892d93   8 weeks ago    187MB
hello-world          latest    d2c94e258dcb   7 months ago   13.3kB
```

🌞 **Lancez un conteneur à partir de l'image Python**

```bash!
[mew@dock compose_test]$ docker ps -all
CONTAINER ID   IMAGE     COMMAND     CREATED          STATUS                      PORTS     NAMES
a64748cf2d51   python    "python3"   20 seconds ago   Exited (0) 19 seconds ago             wizardly_montalcini
```

## 2. Construire une image

Pour construire une image il faut :

- créer un fichier `Dockerfile`
- exécuter une commande `docker build` pour produire une image à partir du `Dockerfile`

🌞 **Ecrire un Dockerfile pour une image qui héberge une application Python**

```
[mew@dock ~]$ cat /home/mew/python_app_build/dockerfile
FROM debian:latest
RUN apt update -y && apt install -y python3 python3-emoji
COPY app.py ./app.py
ENTRYPOINT {"python3", "app.py"}
```

🌞 **Build l'image**

```
[mew@dock python_app_build]$ docker build . -t python_app:version_de_ouf
[+] Building 21.2s (8/8) FINISHED                                       docker:default
 => [internal] load build definition from dockerfile                              0.0s
 => => transferring dockerfile: 230B                                              0.0s
 => [internal] load .dockerignore                                                 0.1s
 => => transferring context: 2B                                                   0.0s
 => [internal] load metadata for docker.io/library/debian:latest                  0.0s
 => [1/3] FROM docker.io/library/debian:latest                                    0.0s
 => [internal] load build context                                                 0.1s
 => => transferring context: 86B                                                  0.0s
 => [2/3] RUN apt update -y && apt install -y python3 python3-emoji              19.8s
 => [3/3] COPY app.py ./app.py                                                    0.1s
 => exporting to image                                                            1.0s
 => => exporting layers                                                           1.0s
 => => writing image sha256:73748dadda98a1fd4d2867cbbd616d0b864f09b25c365970228e  0.0s
 => => naming to docker.io/library/python_app:version_de_ouf                      0.0s
[mew@dock python_app_build]$ docker image ls
REPOSITORY           TAG              IMAGE ID       CREATED              SIZE
python_app           version_de_ouf   73748dadda98   About a minute ago   189MB
```

🌞 **Lancer l'image**

- lance l'image avec `docker run` :

```bash
[mew@dock python_app_build]$ docker run python_app:version_de_ouf
Cet exemple d'application est vraiment naze 👎
```


# III. Docker compose

Pour la fin de ce TP on va manipuler un peu `docker compose`.

🌞 **Créez un fichier `docker-compose.yml`**

```bash!
[mew@dock ~]$ cat /home/mew/compose_test/docker_compose.yml
version: "3"

services:
  conteneur_nul:
    image: debian
    entrypoint: sleep 9999
  conteneur_flopesque:
    image: debian
    entrypoint: sleep 9999
```

🌞 **Lancez les deux conteneurs** avec `docker compose`

- déplacez-vous dans le dossier `compose_test` qui contient le fichier `docker-compose.yml`
- go exécuter `docker compose up -d`

```bash!
[mew@dock compose_test]$ docker compose up -d
[+] Running 3/3
 ✔ conteneur_nul Pulled                                                          12.7s
 ✔ conteneur_flopesque 1 layers [⣿]      0B/0B      Pulled                       12.7s
   ✔ 1b13d4e1a46e Pull complete                                                   4.7s
[+] Running 3/3
 ✔ Network compose_test_default                  Created                          0.4s
 ✔ Container compose_test-conteneur_nul-1        Started                          0.4s
 ✔ Container compose_test-conteneur_flopesque-1  Started                          0.4s
```

> Si tu mets pas le `-d` tu vas perdre la main dans ton terminal, et tu auras les logs des deux conteneurs. `-d` comme *daemon* : pour lancer en tâche de fond.

🌞 **Vérifier que les deux conteneurs tournent**

```
[mew@dock compose_test]$ docker compose ps
NAME                                 IMAGE     COMMAND        SERVICE               CREATED              STATUS              PORTS
compose_test-conteneur_flopesque-1   debian    "sleep 9999"   conteneur_flopesque   About a minute ago   Up About a minute
compose_test-conteneur_nul-1         debian    "sleep 9999"   conteneur_nul         About a minute ago   Up About a minute
```

🌞 **Pop un shell dans le conteneur `conteneur_nul`**

- référez-vous au mémo Docker
- effectuez un `ping conteneur_flopesque` (ouais ouais, avec ce nom là)
  - un conteneur est aussi léger que possible, aucun programme/fichier superflu : t'auras pas la commande `ping` !
  - il faudra installer un paquet qui fournit la commande `ping` pour pouvoir tester
  - juste pour te faire remarquer que les conteneurs ont pas besoin de connaître leurs IP : les noms fonctionnent

```shell!
[mew@dock compose_test]$ docker exec -it compose_test-conteneur_nul-1 sh
# apt update
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
Get:2 http://deb.debian.org/debian bookworm-updates InRelease [52.1 kB]
Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:4 http://deb.debian.org/debian bookworm/main amd64 Packages [8787 kB]
Get:5 http://deb.debian.org/debian bookworm-updates/main amd64 Packages [12.7 kB]
Get:6 http://deb.debian.org/debian-security bookworm-security/main amd64 Packages [134 kB]
Fetched 9185 kB in 2s (3818 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
# apt install inetutils-ping
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  netbase
The following NEW packages will be installed:
  inetutils-ping netbase
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 98.8 kB of archives.
After this operation, 255 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://deb.debian.org/debian bookworm/main amd64 netbase all 6.4 [12.8 kB]
Get:2 http://deb.debian.org/debian bookworm/main amd64 inetutils-ping amd64 2:2.4-2+deb12u1 [86.0 kB]
Fetched 98.8 kB in 0s (248 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package netbase.
(Reading database ... 6098 files and directories currently installed.)
Preparing to unpack .../archives/netbase_6.4_all.deb ...
Unpacking netbase (6.4) ...
Selecting previously unselected package inetutils-ping.
Preparing to unpack .../inetutils-ping_2%3a2.4-2+deb12u1_amd64.deb ...
Unpacking inetutils-ping (2:2.4-2+deb12u1) ...
Setting up netbase (6.4) ...
Setting up inetutils-ping (2:2.4-2+deb12u1) ...
# ping conteneur_flopesque
PING conteneur_flopesque (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: icmp_seq=0 ttl=64 time=0.132 ms
64 bytes from 172.18.0.3: icmp_seq=1 ttl=64 time=0.108 ms
64 bytes from 172.18.0.3: icmp_seq=2 ttl=64 time=0.105 ms
^C--- conteneur_flopesque ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max/stddev = 0.105/0.115/0.132/0.000 ms
```



