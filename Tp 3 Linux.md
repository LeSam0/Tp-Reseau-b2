# Tp 3 Linux


## *I.Etat du Réseaux et Plan du site*

Le Réseaux d'Ynov est constituer d'au moins 3 sous réseaux:
-le LAN WIFI ou tous le monde est lorsqu'il ce connecte au WIFI : WIFI@YNOV et qui est compris entre l'IP 10.33.64.1 et l'IP 10.33.79.254
-le LAN des télés qui est joignable depuis le LAN WIFI et qui est compris entre l'IP 10.33.60.1 et L'IP 10.33.61.254
-le LAN admis 

Nous pensons qu'il doit y avoir d'autre LAN pour chaque éléments connectée au Réseaux d'YNOV, comme un LAN pour les caméras de sécurité et un LAN pour les portiques et les boiters de portes mais nous n'avons pas réussi à y accèder.

**Plan des étages**

[RDC](./Ressource/EtageRDC.png)
[1er](./Ressource/Etage1.png)
[2ème](./Ressource/Etage2.png)
[3ème](./Ressource/Etage3.png)

**Legende :**
- Rouge : Télévision
- Bleu : Borne WIFI
- Orange : Distributeur / Machine à café
- Vert : Porte à Badge
- Violet : Portique
- Noir : PC / Imprimante / Salle avec PC
- Gris : Salle Serveur


PS: nous avons pas cartographier le 4ème étage pour pas déranger l'admin


## II. Liste des Éléments et Vulnérabilité Possible

**Télévision**:

L'ip de chaque télé est static sur le LAN 10.33.61... 

Les télévisions disposent d'une fonction de partage d'écran et nous invite a télécharger une application afin d'utiliser cette fonction. Pour l'installer plusieurs possibilité s'offre a lui, soit par le site officielle 'eshare' qui est sécuriser, soit en tapant l'addresse ip d'une des télés puis en précifiant le port 8000 dans la barre de recherche. Ce qui nous ammène sur la même page que le site eshare mais cette fois ci, nous ne somme pas en https. Ce qui permet a n'importe qui de faire télécharger un exe à toutes les personnes qui essaye de télécharger par ce lien.

**Portique et Boitier porte**

Tous les portiques et le boitier de porte fonctionnes grâce à la technoligie de NFC. Du à manque de moyen, nous n'avons pas pu recuperer le signal émis par les cartes et le téléphones, mais savons que le code de chaque téléphone change régulièrement et pour les badge, nous pensons qu'il est composer d'un code chiffrer qui nous empèche de juste copier la carte pour la réutilliser. 

Pour chaque boitier de porte, ils sont relier au réseaux grâce à des boitiers installer au plafonds dans les couloirs (environs 1 toutes les 2 portes) avec leur adresse MAC indiquer dessus. Nous n'avons pas eu le temps de les trouver dans le réseaux, mais si celle ci sont joignable, il est s'en doute possible d'ouvrir toutes les portes en envoyant une trame présice a ce boitier.

**Caméra de surveillance**

Les Caméras de surveillance sont connecter sur le reseaux, qui doit être distaint lui aussi, soit en connection wifi, mais nous pensont plus quelles sont connectées en filaire.

**Prise RJ45**

Dans tous les couloirs et au souk (et un peu partout dans les salles et le batiments en général), des prises RJ45 sont apparantes dans les mur et même au plafond. Celles des couloirs ne nous donnes aucune connexion, ni IP. En revance, celle du SOUK, nous donne accès au Réseaux des télés et nous donne une IP static.

**Switch**

Un switch reseaux est apparant au niveaux des distributeur du SOUK, celui ci relie la machine a café et le distributeur au réseaux (Nous nous sommes pas brancher dessus pour éviter de tous peter, mais nous pensons qui se connecte soit au réseaux admin, soit à un autre réseaux juste pour les machines).

## III. Scan du Réseaux

Nous avons effectué deux scans dans le LAN 10.33.64.1/20. Le premier a été effectué le 9/11 en pleine après-midi, donc pendant les heures avec le plus de monde connecté aux réseaux, l'autre étant effectué le 10/11 au soir entre 17h15 et 19h30 pendant les heures creuses. 

C'est scan nous on permit de découvrir les machines qui sont connectées au réseau en permanence, et de voir les machines qui sont connectées de manière temporaire grâce au petit script que nous avons fait : [coucou.py](./Ressource/coucou.py).

Le résultat se trouve dans [result_filtered.txt](./Ressource/result_filtered.txt).

A terme, nous pouvons envisager de faire plus approndi de c'est machines pour pouvoir les identifier et les classer dans des catégories (serveur, imprimante, etc...).
