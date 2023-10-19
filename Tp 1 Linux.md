# Tp 1 Linux


## *I. Basics*

**️Carte réseau WiFi :**

l'adresse MAC de la carte WiFi :
```bash!
C:\Users\samyd>getmac /v /fo list

Nom de la connexion: Wi-Fi
Adresse physique:    48-E7-DA-5C-46-3F
```

l'adresse IP de la carte WiFi et le masque de sous-réseau du réseau LAN (format décimal et CIDR):

```bash!
C:\Users\samyd>ipconfig

Carte réseau sans fil Wi-Fi :
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.74.228
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Masque de sous-réseau. . . . . . . . . : 10.33.74.228/20
```

**️ Déso pas déso :**

l'adresse de réseau du LAN : 

10.33.64.0

l'adresse de broadcast : 

10.33.79.255

le nombre d'adresses IP disponibles dans ce réseau :

4094

**Hostname**

le hostname de votre PC:

```bash!
C:\Users\samyd>hostname

LAPTOP-DUFS17OL
```

**Passerelle du réseau**

l'adresse IP de la passerelle du réseau et l'adresse MAC de la passerelle du réseau

```bash!
C:\Users\samyd>ipconfig /all

Carte réseau sans fil Wi-Fi :
  Passerelle par défaut. . . . . . . . . : 10.33.79.254
  
C:\Users\samyd>arp -a
    
    10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
```

**Serveur DHCP et DNS**

l'adresse IP du serveur DHCP et l'adresse IP du serveur DNS 

```bash!
C:\Users\samyd>ipconfig /all

Carte réseau sans fil Wi-Fi :
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                            1.1.1.1
```

**️Table de routage**

la route par défaut

```bash!
C:\Users\samyd>netstat -r

IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.74.228     35
===========================================================================
```

## *II. Go further*

**Hosts ?**

le nom b2.hello.vous corresponde à l'IP 1.1.1.1

C:\Users\samyd>type C:\Windows\System32\drivers\etc\hosts

        1.1.1.1         b2.hello.vous

ping b2.hello.vous ping bien 1.1.1.1

```bash!
C:\Users\samyd>ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
```

**Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo ainsi que le port du serveur auquel vous êtes connectés ainsi que le port que votre PC a ouvert en local pour se connecter au port du serveur distant 

```
C:\Users\samyd>netstat -an

 Proto  Adresse locale         Adresse distante       État
  UDP   0.0.0.0:49664          91.68.245.143:443
```

**Requêtes DNS**

L'adresse IP correspondant au nom de domaine www.ynov.com est : 

```
C:\Users\samyd>nslookup www.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:ae9
          2606:4700:20::ac43:4ae2
          2606:4700:20::681a:be9
          172.67.74.226
          104.26.10.233
          104.26.11.233
```

Le nom de domaine correspond a l'IP 174.43.238.89 est :

```
C:\Users\samyd>nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

**Hop hop hop**

Mes paquets passent par 9 machines quand j'essaye de joindre www.ynov.com

```
C:\Users\samyd>tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.10.233]
avec un maximum de 30 sauts :

  1     4 ms     4 ms     1 ms  10.33.79.254
  2     3 ms     3 ms     3 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     3 ms     8 ms     1 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     3 ms     2 ms     2 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    37 ms    10 ms    32 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    10 ms     9 ms    10 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    59 ms    10 ms    10 ms  141.101.67.48
  8    11 ms    11 ms    19 ms  141.101.67.54
  9     *       11 ms     9 ms  104.26.10.233

Itinéraire déterminé.
```

**IP publique**

l'adresse IP publique de la passerelle du réseau 

```
C:\Users\samyd>nslookup myip.opendns.com resolver1.opendns.com
Serveur :   dns.opendns.com
Address:  208.67.222.222

Réponse ne faisant pas autorité :
Nom :    myip.opendns.com
Address:  195.7.117.146
```

**Scan réseau**

//

il y a  machines dans le LAN auquel je suis connectés

## *III. Le requin*

**Capture ARP**

filtre : arp

[Lien vers capture ARP](./Ressource/arp.pcapng)

**Capture DNS**

filtre : dns

[Lien vers capture DNS](./Ressource/dns.pcapng)

**Capture TCP**

filtre : tcp

[Lien vers capture TCP](./Ressource/tcp.pcapng)