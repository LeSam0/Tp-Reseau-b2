# TP7 SECU : Accès réseau sécurisé

# I. VPN

🌞 **Monter un serveur VPN Wireguard sur `vpn.tp7.secu`**
```bash!
[mew@vpn ~]$ sudo modprobe wireguard
[mew@vpn ~]$ echo wireguard | sudo tee /etc/modules-load.d/wireguard.conf
wireguard
[mew@vpn ~]$ sudo cat /etc/sysctl.conf
sysctl.conf(5) and sysctl.d(5).
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1
[mew@vpn ~]$ sudo dnf install wireguard-tools -y
Complete!
[mew@vpn ~]$ wg genkey | sudo tee /etc/wireguard/server.key
sFqlzUBWPnON1a+GhpphafnQlp1M3d4VfHqp2C/67VY=
[mew@vpn ~]$ sudo chmod 0400 /etc/wireguard/server.key
[mew@vpn ~]$ sudo cat /etc/wireguard/server.key | wg pubkey | sudo tee /etc/wireguard/server.pub
Xb/MZopMs3jvfK8J4oQXqyLf3UdHzAr5zCJL60FV9h8=
[mew@vpn ~]$ sudo mkdir -p /etc/wireguard/clients
[mew@vpn ~]$ wg genkey | sudo tee /etc/wireguard/clients/martine.key
IMp9Vxfb0tLuLATm9kH7aCbrTvy51HYrVnDJL2JGCEo=
[mew@vpn ~]$ sudo chmod 0400 /etc/wireguard/clients/martine.key
[mew@vpn ~]$ sudo cat /etc/wireguard/clients/martine.key | wg pubkey | sudo tee /etc/wireguard
/clients/martine.pub
xJ8LZ4ut2p+nVIBWnFTsXQa2i7pChu/Wm7i7HbuWM1I=mew

[mew@vpn etc]$ sudo cat /etc/wireguard/wg0.conf
[Interface]
Address = 10.107.1.0/24
SaveConfig = false
PostUp = firewall-cmd --zone=public --add-masquerade
PostUp = firewall-cmd --add-interface=wg0 --zone=public
PostDown = firewall-cmd --zone=public --remove-masquerade
PostDown = firewall-cmd --remove-interface=wg0 --zone=public
ListenPort = 13337
PrivateKey = sFqlzUBWPnON1a+GhpphafnQlp1M3d4VfHqp2C/67VY=

[Peer]
PublicKey = xJ8LZ4ut2p+nVIBWnFTsXQa2i7pChu/Wm7i7HbuWM1I=
AllowedIPs = 10.107.1.11/32
[mew@vpn ~]$ sudo systemctl status wg-quick@wg0.service
● wg-quick@wg0.service - WireGuard via wg-quick(8) for wg0
     Loaded: loaded (/usr/lib/systemd/system/wg-quick@.service; disabled; preset: disa>
     Active: active (exited) since Fri 2024-01-26 15:21:52 CET; 4s ago
       Docs: man:wg-quick(8)
             man:wg(8)
             https://www.wireguard.com/
             https://www.wireguard.com/quickstart/
             https://git.zx2c4.com/wireguard-tools/about/src/man/wg-quick.8
             https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8
    Process: 1240 ExecStart=/usr/bin/wg-quick up wg0 (code=exited, status=0/SUCCESS)
   Main PID: 1240 (code=exited, status=0/SUCCESS)
        CPU: 244ms

Jan 26 15:21:52 dock systemd[1]: Starting WireGuard via wg-quick(8) for wg0...
Jan 26 15:21:52 dock wg-quick[1240]: [#] ip link add wg0 type wireguard
Jan 26 15:21:52 dock wg-quick[1240]: [#] wg setconf wg0 /dev/fd/63
Jan 26 15:21:52 dock wg-quick[1240]: [#] ip -4 address add 10.7.2.0/24 dev wg0
Jan 26 15:21:52 dock wg-quick[1240]: [#] ip link set mtu 1420 up dev wg0
Jan 26 15:21:52 dock wg-quick[1240]: [#] firewall-cmd --zone=public --add-masquerade
Jan 26 15:21:52 dock wg-quick[1276]: success
Jan 26 15:21:52 dock wg-quick[1240]: [#] firewall-cmd --add-interface=wg0 --zone=public
Jan 26 15:21:52 dock wg-quick[1283]: success
Jan 26 15:21:52 dock systemd[1]: Finished WireGuard via wg-quick(8) for wg0.

```

🌞 **Client Wireguard sur `martine.tp7.secu`**

```bash!
[mew@martine ~]$ sudo dnf install wireguard-tools
Complete!
[mew@martine ~]$ sudo ip route del default
[mew@martine ~]$ ping 1.1.1.1
ping: connect: Network is unreachable
[mew@martine wireguard]$ cat /home/mew/wireguard/martine.conf
[Interface]
Address = 10.7.2.11/24
PrivateKey = IMp9Vxfb0tLuLATm9kH7aCbrTvy51HYrVnDJL2JGCEo=

[Peer]
PublicKey = Xb/MZopMs3jvfK8J4oQXqyLf3UdHzAr5zCJL60FV9h8=
AllowedIPs = 0.0.0.0/0
Endpoint = 10.7.1.100:13337
[mew@martine wireguard]$ wg-quick up ./martine.conf
Warning: `/home/mew/wireguard/martine.conf' is world accessible
[#] ip link add martine type wireguard
[#] wg setconf martine /dev/fd/63
[#] ip -4 address add 10.7.2.11/24 dev martine
[#] ip link set mtu 65456 up dev martine
[#] wg set martine fwmark 51820
[#] ip -4 route add 0.0.0.0/0 dev martine table 51820
[#] ip -4 rule add not fwmark 51820 table 51820
[#] ip -4 rule add table main suppress_prefixlength 0
[#] sysctl -q net.ipv4.conf.all.src_valid_mark=1
[#] nft -f /dev/fd/63
```

🌞 **Client Wireguard sur votre PC**

```bash!
[Interface]
PrivateKey = wKdumCYryyIr540X9h1CZLw/mDnspbNF+nJHoPYIjms=
Address = 10.7.2.100/24

[Peer]
PublicKey = /kOPAz5WW0IQR/dBJyT8ci10x/9KBq6VwjILQ/Nv4gE=
AllowedIPs = 10.7.2.0/24
Endpoint = 10.7.1.100:13337
```

# II. SSH

## 1. Setup

```bash!
[mew@web ~]$ ping 10.7.2.11
64 bytes from 10.7.2.11: icmp_seq=5 ttl=63 time=2.86 ms
[mew@web ~]$ ping 10.7.2.100
PING 10.7.2.100 (10.7.2.100) 56(84) bytes of data.
64 bytes from 10.7.2.100: icmp_seq=1 ttl=127 time=1.72 ms
```

## 3. Connexion par clé

🌞 **Générez une nouvelle paire de clés pour ce TP**

Pareil pour toute les vm 
```bash!
 C:\Users\samyd>ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\samyd/.ssh/id_ed25519):
C:\Users\samyd/.ssh/id_ed25519 already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\samyd/.ssh/id_ed25519
Your public key has been saved in C:\Users\samyd/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:Y+AGg5I5lcp0nqa86GFusG76Kl64yvuro0MTxTPtPHg samyd@LAPTOP-DUFS17OL
The key's randomart image is:
+--[ED25519 256]--+
|  o..            |
| =.B .           |
|B.= X .          |
|.= = E .         |
|. + . + S        |
|.=.  . . .       |
|+=o.             |
|O=+              |
|/&*o.            |
+----[SHA256]-----+
samyd@LAPTOP-DUFS17OL MINGW64 ~ (main)
$ ssh-copy-id mew@10.7.1.100
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/c/Users/samyd/.ssh/id_ed25519.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
mew@10.7.1.100's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'mew@10.7.1.100'"
and check to make sure that only the key(s) you wanted were added.


samyd@LAPTOP-DUFS17OL MINGW64 ~ (main)
$ ssh mew@10.7.1.100
Enter passphrase for key '/c/Users/samyd/.ssh/id_ed25519':
Last login: Fri Jan 26 15:25:04 2024 from 10.7.1.1
[mew@vpn ~]$ 
```

## 4. Conf serveur SSH

🌞 **Changez l'adresse IP d'écoute**

pareil sur toute les machines en changant les ip

```bash!
[mew@vpn ~]$ sudo cat /etc/ssh/sshd_config
ListenAddress 10.7.2.0
```

🌞 **Améliorer le niveau de sécurité du serveur**
[config ssh](./Ressource/config_ssh.txt)


# III. HTTP

## 1. Initial setup

🌞 **Monter un bête serveur HTTP sur `web.tp7.secu`**

```nginx
server {
    server_name web.tp7.secu;

    listen 10.1.1.1:80;

    # vous collez un ptit index.html dans ce dossier et zou !
    root /var/www/site_nul;
}
```

🌞 **Site web joignable qu'au sein du réseau VPN**

- le site web ne doit écouter que sur l'IP du réseau VPN
- le trafic à destination du port 80 n'est autorisé que si la requête vient du réseau VPN (firewall)
- prouvez qu'il n'est pas possible de joindre le site sur son IP host-only

🌞 **Accéder au site web**

- depuis votre PC, avec un `curl`
- vous êtes normalement obligés d'être co au VPN pour accéder au site

## 2. Génération de certificat et HTTPS

### A. Préparation de la CA

On va commencer par générer la clé et le certificat de notre Autorité de Certification (CA). Une fois fait, on pourra s'en servir pour signer d'autres certificats, comme celui de notre serveur web.

Pour que la connexion soit trusted, il suffira alors d'ajouter le certificat de notre CA au magasin de certificats de votre navigateur sur votre PC.

🌞 **Générer une clé et un certificat de CA**

```bash
# mettez des infos dans le prompt, peu importe si c'est fake
# on va vous demander un mot de passe pour chiffrer la clé aussi
$ openssl genrsa -des3 -out CA.key 4096
$ openssl req -x509 -new -nodes -key CA.key -sha256 -days 1024  -out CA.pem
$ ls
# le pem c'est le certificat (clé publique)
# le key c'est la clé privée
```

### B. Génération du certificat pour le serveur web

Il est temps de générer une clé et un certificat que notre serveur web pourra utiliser afin de proposer une connexion HTTPS.

🌞 **Générer une clé et une demande de signature de certificat pour notre serveur web**

```bash
$ openssl req -new -nodes -out web.tp7.secu.csr -newkey rsa:4096 -keyout web.tp7.secu.key
$ ls
# web.tp7.secu.csr c'est la demande de signature
# web.tp7.secu.key c'est la clé qu'utilisera le serveur web
```

🌞 **Faire signer notre certificat par la clé de la CA**

- préparez un fichier `v3.ext` qui contient :

```ext
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = web.tp7.secu
DNS.2 = www.tp7.secu
```

- effectuer la demande de signature pour récup un certificat signé par votre CA :

```bash
$ openssl x509 -req -in web.tp7.secu.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out web.tp7.secu.crt -days 500 -sha256 -extfile v3.ext
$ ls
# web.tp7.secu.crt c'est le certificat qu'utilisera le serveur web
```

### C. Bonnes pratiques RedHat

Sur RedHat, il existe un emplacement réservé aux clés et certificats :

- `/etc/pki/tls/certs/` pour les certificats
  - pas choquant de voir du droit de lecture se balader
- `/etc/pki/tls/private/` pour les clés
  - ici, seul le propriétaire du fichier a le droit de lecture

🌞 **Déplacer les clés et les certificats dans l'emplacement réservé**

- gérez correctement les permissions de ces fichiers

### D. Config serveur Web

🌞 **Ajustez la configuration NGINX**

- le site web doit être disponible en HTTPS en utilisant votre clé et votre certificat
- une conf minimale ressemble à ça :

```nginx
server {
    server_name web.tp7.secu;

    listen 10.7.1.103:443 ssl;

    ssl_certificate /etc/pki/tls/certs/web.tp7.secu.crt;
    ssl_certificate_key /etc/pki/tls/private/web.tp7.secu.key;
    
    root /var/www/site_nul;
}
```

🌞 **Prouvez avec un `curl` que vous accédez au site web**

- depuis votre PC
- avec un `curl -k` car il ne reconnaît pas le certificat là

🌞 **Ajouter le certificat de la CA dans votre navigateur**

- vous pourrez ensuite visitez `https://web.tp7.b2` sans alerte de sécurité, et avec un cadenas vert
- il faut aussi ajouter l'IP de la machine à votre fichier `hosts` pour qu'elle corresponde au nom `web.tp7.b2`

> *En entreprise, c'est comme ça qu'on fait pour qu'un certificat de CA non-public soit trusted par tout le monde : on dépose le certificat de CA dans le navigateur (et l'OS) de tous les PCs. Evidemment, on utilise une technique de déploiement automatisé aussi dans la vraie vie, on l'ajoute pas à la main partout hehe.*

### E. Bonus renforcement TLS

⭐ **Bonus : renforcer la conf TLS**

- faites quelques recherches pour forcer votre serveur à n'utiliser que des méthodes de chiffrement fortes
- ça implique de refuser les connexions SSL, ou TLS 1.0, on essaie de forcer TLS 1.3

