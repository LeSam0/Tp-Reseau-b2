# TP 6 Linux

## *I. DNS Rebinding*

**Write-up de l'épreuve**

Le challenge nous annène sur une page web qui nous demande  de rentrer une adresse web comme www.google.com ou une ip et nous affiche le resultat dans une iframe. Un code nous est donner et on comprend que il y a plusieur check pour afficher le resultat, savoir si ip ou l'addresse qu'on donne existe et si elle est public par exemple. 

Pour réussir ce chall, on comprend qui va falloir passer tous les verifs en envoyant l'adresse loopback (127.0.0.1) sur le /admin sur le port 54022 tous en ayant pas de token.

La technique utiliser pour ce chall est le DNS Rebinding, c'est a dire faire croire au navigateur que l’adresse IP à contacter pour accéder au site http://attacker.com/ n’est plus celle du site de l’attaquant, mais celle que l'on souhaite.

Pour cela, on a utilider un site qui nous donne l'input a donner au site a savoir :

```
7f000001.08080808.rbndr.us
```

En spammant un peu, cela nous permet d'accèder a l'iframe du flag.

**Proposer une version du code qui n'est pas vulnérable**

Commande nmap : 

## *II. Netfilter erreurs courantes*

**Write-up de l'épreuve**

Pour ce chall, on nous donne accès a une page web qui nous demande d'accèder a une autre page mais ou les règles de firewall son "bien configurer", en appuyant sur la phrase en bas a droite de la page, cela nous télécharge un fichier, ce ficher est les règles du firewall. On comprend que l'on doit être accepté sur une ligne pour rentrer. 

En lisant les lignes on remarque une ligne : 

```
IP46T -A INPUT-FINAL -m limit --limit 2/sec --limit-burst 2 -j LOG --log-prefix 'FW_INPUT_DROP '
```

celle ci nous permet d'être accepté que si on spam la connexion.

**Proposer une version du code qui n'est pas vulnérable**

## *III. ARP Spoofing Ecoute active*

**Write-up de l’épreuve**

**Proposer une version du code qui n’est pas vulnérable**

## *IV. Bonus : Trafic Global System for Mobile communications*

**Write-up de l’épreuve**

Pour cette épreuve, on nous donne une capture wireshark qui a première vue nous donne pas grand chose. Cela dit, le non du chall nous dit que c'est dit GSM un protocole de communication de téléphone. On remarque aussi une trame avec 128 bites de data. 

En mettant en relation toutes c'est information, on me imagine un protocole de communication sur téléphone commme les SMS. Apres deux trois recherche on peut trouver un déchirement pour un protocole de SMS qui nous donne le flag. 