# TP3 : Linux Hardening

## 1. Guides CIS


🌞 **Suivre un guide CIS**

- vous devez faire :
  - la section 2.1
  2.1.1
  ```
  [mew@dock ~]$ sudo dnf install chrony
  Last metadata expiration check: 0:02:53 ago on Thu 11 Jan 2024  02:36:50 PM CET.
  Package chrony-4.3-1.el9.x86_64 is already installed.
  Dependencies resolved.
  Nothing to do.
  Complete!
  ```
  2.1.2
  ```
  [mew@dock ~]$ grep -E "^(server|pool)" /etc/chrony.conf
  server <remote-server>
  [mew@dock ~]$  grep ^OPTIONS /etc/sysconfig/chronyd
  OPTIONS="-u chrony"  
  ```
  - les sections 3.1 3.2 et 3.3
    
   3.1.1
```
    
```
    3.1.2
  ```
  
  ```
    3.1.3
  ```
  
  ```
    3.2.1
  ```
  
  ```
    3.2.2
  ```
  
  ```
    3.3.1
  ```
  
  ```
    3.3.2
  ```
  
  ```
    3.3.3
  ```
  
  ```
    3.3.4
  ```
  
  ```
    3.3.5
  ```
  
  ```
    3.3.6
    ```
    ```
    3.3.7
    ```
  
    ```
    3.3.8
    ```
    ```
    3.3.9
    ```
  
    ```  
  - toute la section 5.2 Configure SSH Server
  
  5.2.1
  ```
  
  ```
  5.2.2
  ```
  
  ```
  5.2.3
  ```
  
  ```
  5.2.4
  ```
  
  ```
  5.2.5
  ```
  
  ```
  5.2.6
  ```
  
  ```
  5.2.7
  ```
  
  ```
  5.2.8
  ```
  
  ```
  5.2.9
  ```
  
  ```
  5.2.10
  ```
  
  ```
  5.2.11
  ```
  
  ```
  5.2.12
  ```
  
  ```
  5.2.13
  ```
  
  ```
  5.2.14
  ```
  
  ```
  5.2.15
  ```
  
  ```
  5.2.16
  ```
  
  ```
  5.2.17
  ```
  
  ```
  5.2.18
  ```
  
  ```
  5.2.19
  ```
  
  ```
  5.2.20
  ```
  
  ```
  - au moins 10 points dans la section 6.1 System File Permissions

    6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  6.1.1
  ```
  
  ```
  - au moins 10 points ailleur sur un truc que vous trouvez utile

## 2. Conf SSH

🌞 **Chiffrement fort côté serveur**

- trouver une ressource de confiance (je veux le lien en compte-rendu)

- configurer le serveur SSH pour qu'il utilise des paramètres forts en terme de chiffrement (je veux le fichier de conf dans le compte-rendu)
  - conf dans le fichier de conf
  [source](https://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html)
  [config ssh](./Ressource/config_ssh.txt)
  - regénérer des clés pour le serveur ?
  [source](https://www.malekal.com/generer-et-se-connecter-en-ssh-avec-des-cles-ssh/)
```
[mew@dock ~]$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/mew/.ssh/id_ed25519):
Created directory '/home/mew/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/mew/.ssh/id_ed25519
Your public key has been saved in /home/mew/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:0iH5zExGFhkcv3Ac4KALh0ZM6kD3yMn0777bPtPSl48 mew@dock
The key's randomart image is:
+--[ED25519 256]--+
| +oo  ..B*.      |
|.o*.=. *oo .     |
|o +=ooo * +      |
|o. o ..X + .     |
| .  . ..S .      |
|      ..         |
|       .  o   .  |
|      . .+ o o.  |
|       ++o+ .E.. |
+----[SHA256]-----+
  ```
  - regénérer les paramètres Diffie-Hellman ? (se renseigner sur Diffie-Hellman ?)
et
🌞 **Clés de chiffrement fortes pour le client**

- trouver une ressource de confiance (je veux le lien en compte-rendu)
- générez-vous une paire de clés qui utilise un chiffrement fort et une passphrase
[source](https://www.it-connect.fr/chapitres/authentification-ssh-par-cles/) 
```
PS C:\Users\samyd> ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\samyd/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\samyd/.ssh/id_ed25519
Your public key has been saved in C:\Users\samyd/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:D1jqDaW+UtU+3T6j0HKqmxzsJO8N73A5If+i5zjfHsk samyd@LAPTOP-DUFS17OL
The key's randomart image is:
+--[ED25519 256]--+
|                 |
|                 |
|        o.       |
|       *. .      |
|      =.S... .   |
|     o.+ =o=...  |
|     .+ B O.E.   |
|    .  B.XoO .+  |
|     ...@XBo=. o |
+----[SHA256]-----+
$ ssh-copy-id mew@10.7.1.10
```

🌞 **Connectez-vous en SSH à votre VM avec cette paire de clés**

- prouvez en ajoutant `-vvvv` sur la commande `ssh` de connexion que vous utilisez bien cette clé là

```
C:\Users\samyd>ssh mew@10.7.1.10 -p 8080 -vvvv
OpenSSH_for_Windows_8.6p1, LibreSSL 3.4.3
debug3: Failed to open file:C:/Users/samyd/.ssh/config error:2
debug3: Failed to open file:C:/ProgramData/ssh/ssh_config error:2
debug2: resolve_canonicalize: hostname 10.7.1.10 is address
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> 'C:\\Users\\samyd/.ssh/known_hosts'
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> 'C:\\Users\\samyd/.ssh/known_hosts2'
debug1: Authenticator provider $SSH_SK_PROVIDER did not resolve; disabling
debug3: ssh_connect_direct: entering
debug1: Connecting to 10.7.1.10 [10.7.1.10] port 8080.
debug1: Connection established.
debug3: Failed to open file:C:/Users/samyd/.ssh/id_rsa error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_rsa.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_rsa error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_rsa type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_rsa-cert error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_rsa-cert.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_rsa-cert error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_rsa-cert type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_dsa error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_dsa.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_dsa error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_dsa type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_dsa-cert error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_dsa-cert.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_dsa-cert error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_dsa-cert type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_ecdsa error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_ecdsa type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa-cert error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa-cert.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_ecdsa-cert error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_ecdsa-cert type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa_sk error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa_sk.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_ecdsa_sk error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_ecdsa_sk type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa_sk-cert error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ecdsa_sk-cert.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_ecdsa_sk-cert error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_ecdsa_sk-cert type -1
debug1: identity file C:\\Users\\samyd/.ssh/id_ed25519 type 3
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ed25519-cert error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ed25519-cert.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_ed25519-cert error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_ed25519-cert type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ed25519_sk error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ed25519_sk.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_ed25519_sk error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_ed25519_sk type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ed25519_sk-cert error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_ed25519_sk-cert.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_ed25519_sk-cert error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_ed25519_sk-cert type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_xmss error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_xmss.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_xmss error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_xmss type -1
debug3: Failed to open file:C:/Users/samyd/.ssh/id_xmss-cert error:2
debug3: Failed to open file:C:/Users/samyd/.ssh/id_xmss-cert.pub error:2
debug3: failed to open file:C:/Users/samyd/.ssh/id_xmss-cert error:2
debug1: identity file C:\\Users\\samyd/.ssh/id_xmss-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_for_Windows_8.6
debug1: Remote protocol version 2.0, remote software version OpenSSH_8.7
debug1: compat_banner: match: OpenSSH_8.7 pat OpenSSH* compat 0x04000000
debug2: fd 3 setting O_NONBLOCK
debug1: Authenticating to 10.7.1.10:8080 as 'mew'
debug3: put_host_port: [10.7.1.10]:8080
debug3: Failed to open file:C:/Users/samyd/.ssh/known_hosts2 error:2
debug1: load_hostkeys: fopen C:\\Users\\samyd/.ssh/known_hosts2: No such file or directory
debug3: Failed to open file:C:/ProgramData/ssh/ssh_known_hosts error:2
debug1: load_hostkeys: fopen __PROGRAMDATA__\\ssh/ssh_known_hosts: No such file or directory
debug3: Failed to open file:C:/ProgramData/ssh/ssh_known_hosts2 error:2
debug1: load_hostkeys: fopen __PROGRAMDATA__\\ssh/ssh_known_hosts2: No such file or directory
debug3: order_hostkeyalgs: no algorithms matched; accept original
debug3: send packet: type 20
debug1: SSH2_MSG_KEXINIT sent
debug3: receive packet: type 20
debug1: SSH2_MSG_KEXINIT received
debug2: local client KEXINIT proposal
debug2: KEX algorithms: curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,ext-info-c
debug2: host key algorithms: ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,ssh-ed25519,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,rsa-sha2-512,rsa-sha2-256,ssh-rsa
debug2: ciphers ctos: chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com
debug2: ciphers stoc: chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com
debug2: MACs ctos: umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1
debug2: MACs stoc: umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1
debug2: compression ctos: none,zlib@openssh.com,zlib
debug2: compression stoc: none,zlib@openssh.com,zlib
debug2: languages ctos:
debug2: languages stoc:
debug2: first_kex_follows 0
debug2: reserved 0
debug2: peer server KEXINIT proposal
debug2: KEX algorithms: curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512
debug2: host key algorithms: rsa-sha2-512,rsa-sha2-256,ecdsa-sha2-nistp256,ssh-ed25519
debug2: ciphers ctos: aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr
debug2: ciphers stoc: aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr
debug2: MACs ctos: hmac-sha2-256-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha1,umac-128@openssh.com,hmac-sha2-512
debug2: MACs stoc: hmac-sha2-256-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha1,umac-128@openssh.com,hmac-sha2-512
debug2: compression ctos: none,zlib@openssh.com
debug2: compression stoc: none,zlib@openssh.com
debug2: languages ctos:
debug2: languages stoc:
debug2: first_kex_follows 0
debug2: reserved 0
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ssh-ed25519
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug3: send packet: type 30
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug3: receive packet: type 31
debug1: SSH2_MSG_KEX_ECDH_REPLY received
debug1: Server host key: ssh-ed25519 SHA256:DSqIxzjBc01DQ/Fw5GiBiAxUpeKcg1ic0zyEoccPx40
debug3: put_host_port: [10.7.1.10]:8080
debug3: put_host_port: [10.7.1.10]:8080
debug3: Failed to open file:C:/Users/samyd/.ssh/known_hosts2 error:2
debug1: load_hostkeys: fopen C:\\Users\\samyd/.ssh/known_hosts2: No such file or directory
debug3: Failed to open file:C:/ProgramData/ssh/ssh_known_hosts error:2
debug1: load_hostkeys: fopen __PROGRAMDATA__\\ssh/ssh_known_hosts: No such file or directory
debug3: Failed to open file:C:/ProgramData/ssh/ssh_known_hosts2 error:2
debug1: load_hostkeys: fopen __PROGRAMDATA__\\ssh/ssh_known_hosts2: No such file or directory
debug1: checking without port identifier
debug3: record_hostkey: found key type ED25519 in file C:\\Users\\samyd/.ssh/known_hosts:16
debug3: record_hostkey: found key type RSA in file C:\\Users\\samyd/.ssh/known_hosts:17
debug3: record_hostkey: found key type ECDSA in file C:\\Users\\samyd/.ssh/known_hosts:18
debug3: load_hostkeys_file: loaded 3 keys from 10.7.1.10
debug3: Failed to open file:C:/Users/samyd/.ssh/known_hosts2 error:2
debug1: load_hostkeys: fopen C:\\Users\\samyd/.ssh/known_hosts2: No such file or directory
debug3: Failed to open file:C:/ProgramData/ssh/ssh_known_hosts error:2
debug1: load_hostkeys: fopen __PROGRAMDATA__\\ssh/ssh_known_hosts: No such file or directory
debug3: Failed to open file:C:/ProgramData/ssh/ssh_known_hosts2 error:2
debug1: load_hostkeys: fopen __PROGRAMDATA__\\ssh/ssh_known_hosts2: No such file or directory
debug1: Host '10.7.1.10' is known and matches the ED25519 host key.
debug1: Found key in C:\\Users\\samyd/.ssh/known_hosts:16
debug1: found matching key w/out port
debug1: check_host_key: hostkey not known or explicitly trusted: disabling UpdateHostkeys
debug3: send packet: type 21
debug2: set_newkeys: mode 1
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug3: receive packet: type 21
debug1: SSH2_MSG_NEWKEYS received
debug2: set_newkeys: mode 0
debug1: rekey in after 134217728 blocks
debug3: unable to connect to pipe \\\\.\\pipe\\openssh-ssh-agent, error: 2
debug1: pubkey_prepare: ssh_get_authentication_socket: No such file or directory
debug1: Will attempt key: C:\\Users\\samyd/.ssh/id_rsa
debug1: Will attempt key: C:\\Users\\samyd/.ssh/id_dsa
debug1: Will attempt key: C:\\Users\\samyd/.ssh/id_ecdsa
debug1: Will attempt key: C:\\Users\\samyd/.ssh/id_ecdsa_sk
debug1: Will attempt key: C:\\Users\\samyd/.ssh/id_ed25519 ED25519 SHA256:D1jqDaW+UtU+3T6j0HKqmxzsJO8N73A5If+i5zjfHsk
debug1: Will attempt key: C:\\Users\\samyd/.ssh/id_ed25519_sk
debug1: Will attempt key: C:\\Users\\samyd/.ssh/id_xmss
debug2: pubkey_prepare: done
debug3: send packet: type 5
debug3: receive packet: type 7
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com,webauthn-sk-ecdsa-sha2-nistp256@openssh.com>
debug3: receive packet: type 6
debug2: service_accept: ssh-userauth
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug3: send packet: type 50
debug3: receive packet: type 51
debug1: Authentications that can continue: publickey
debug3: start over, passed a different list publickey
debug3: preferred publickey,keyboard-interactive,password
debug3: authmethod_lookup publickey
debug3: remaining preferred: keyboard-interactive,password
debug3: authmethod_is_enabled publickey
debug1: Next authentication method: publickey
debug1: Trying private key: C:\\Users\\samyd/.ssh/id_rsa
debug3: no such identity: C:\\Users\\samyd/.ssh/id_rsa: No such file or directory
debug1: Trying private key: C:\\Users\\samyd/.ssh/id_dsa
debug3: no such identity: C:\\Users\\samyd/.ssh/id_dsa: No such file or directory
debug1: Trying private key: C:\\Users\\samyd/.ssh/id_ecdsa
debug3: no such identity: C:\\Users\\samyd/.ssh/id_ecdsa: No such file or directory
debug1: Trying private key: C:\\Users\\samyd/.ssh/id_ecdsa_sk
debug3: no such identity: C:\\Users\\samyd/.ssh/id_ecdsa_sk: No such file or directory
debug1: Offering public key: C:\\Users\\samyd/.ssh/id_ed25519 ED25519 SHA256:D1jqDaW+UtU+3T6j0HKqmxzsJO8N73A5If+i5zjfHsk
debug3: send packet: type 50
debug2: we sent a publickey packet, wait for reply
debug3: receive packet: type 60
debug1: Server accepts key: C:\\Users\\samyd/.ssh/id_ed25519 ED25519 SHA256:D1jqDaW+UtU+3T6j0HKqmxzsJO8N73A5If+i5zjfHsk
debug3: sign_and_send_pubkey: ED25519 SHA256:D1jqDaW+UtU+3T6j0HKqmxzsJO8N73A5If+i5zjfHsk
debug3: sign_and_send_pubkey: signing using ssh-ed25519 SHA256:D1jqDaW+UtU+3T6j0HKqmxzsJO8N73A5If+i5zjfHsk
Enter passphrase for key 'C:\Users\samyd/.ssh/id_ed25519':
debug3: send packet: type 50
debug3: receive packet: type 52
debug1: Authentication succeeded (publickey).
Authenticated to 10.7.1.10 ([10.7.1.10]:8080).
debug1: channel 0: new [client-session]
debug3: ssh_session2_open: channel_new: 0
debug2: channel 0: send open
debug3: send packet: type 90
debug1: Requesting no-more-sessions@openssh.com
debug3: send packet: type 80
debug1: Entering interactive session.
debug1: pledge: network
debug1: ENABLE_VIRTUAL_TERMINAL_INPUT is supported. Reading the VTSequence from console
debug3: This windows OS supports conpty
debug1: ENABLE_VIRTUAL_TERMINAL_PROCESSING is supported. Console supports the ansi parsing
debug3: Successfully set console output code page from:65001 to 65001
debug3: Successfully set console input code page from:850 to 65001
debug3: receive packet: type 80
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug3: receive packet: type 4
debug1: Remote: /home/mew/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug3: receive packet: type 4
debug1: Remote: /home/mew/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug3: receive packet: type 91
debug2: channel_input_open_confirmation: channel 0: callback start
debug2: fd 3 setting TCP_NODELAY
debug2: client_session2_setup: id 0
debug2: channel 0: request pty-req confirm 1
debug3: send packet: type 98
debug2: channel 0: request shell confirm 1
debug3: send packet: type 98
debug2: channel_input_open_confirmation: channel 0: callback done
debug2: channel 0: open confirm rwindow 0 rmax 32768
debug3: receive packet: type 99
debug2: channel_input_status_confirm: type 99 id 0
debug2: PTY allocation request accepted on channel 0
debug2: channel 0: rcvd adjust 2097152
debug3: receive packet: type 99
debug2: channel_input_status_confirm: type 99 id 0
debug2: shell request accepted on channel 0
```

## 4. DoT

🌞 **Configurer la machine pour qu'elle fasse du DoT**

- installez `systemd-networkd` sur la machine pour ça
```
[mew@dock etc]$ sudo dnf install systemd-resolved
Rocky Linux 9 - BaseOS                                 4.3 kB/s | 4.1 kB     00:00
Rocky Linux 9 - BaseOS                                 1.0 MB/s | 2.2 MB     00:02
Rocky Linux 9 - AppStream                              5.1 kB/s | 4.5 kB     00:00
Rocky Linux 9 - AppStream                              2.6 MB/s | 7.4 MB     00:02
Rocky Linux 9 - Extras                                 5.8 kB/s | 2.9 kB     00:00
Dependencies resolved.
=======================================================================================
 Package                   Architecture    Version               Repository       Size
=======================================================================================
Installing:
 systemd-resolved          x86_64          252-18.el9            baseos          361 k

Transaction Summary
=======================================================================================
Install  1 Package

Total download size: 361 k
Installed size: 787 k
Is this ok [y/N]: y
Downloading Packages:
systemd-resolved-252-18.el9.x86_64.rpm                 446 kB/s | 361 kB     00:00
---------------------------------------------------------------------------------------
Total                                                  278 kB/s | 361 kB     00:01
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                               1/1
  Running scriptlet: systemd-resolved-252-18.el9.x86_64                            1/1
  Installing       : systemd-resolved-252-18.el9.x86_64                            1/1
  Running scriptlet: systemd-resolved-252-18.el9.x86_64                            1/1
  Verifying        : systemd-resolved-252-18.el9.x86_64                            1/1

Installed:
  systemd-resolved-252-18.el9.x86_64

Complete!
```
- activez aussi DNSSEC tant qu'on y est
- référez-vous à cette doc qui est cool par exemple
- utilisez le serveur public de CloudFlare : 1.1.1.1 (il supporte le DoT)

    [Fichier conf](./Ressource/conf-dot.txt)

🌞 **Prouvez que les requêtes DNS effectuées par la machine...**

- ont une réponse qui provient du serveur que vous avez conf (normalement c'est `127.0.0.1` avec `systemd-networkd` qui tourne)
  - quand on fait un `dig ynov.com` on voit en bas quel serveur a répondu
- mais qu'en réalité, la requête a été forward vers 1.1.1.1 avec du TLS
  - je veux une capture Wireshark à l'appui !
  [Capture DoT](./Ressource/dot.txt)

## 5. AIDE

🌞 **Installer et configurer AIDE**

- configurez AIDE pour qu'il surveille (fichier de conf en compte-rendu)
  - le fichier de conf du serveur SSH
  - le fichier de conf du client chrony (le service qui gère le temps)
  - le fichier de conf de `systemd-networkd`

    [Fichier conf](./Ressource/conf-aide.txt)
    
🌞 **Scénario de modification**

- introduisez une modification dans le fichier de conf Chrony
- montrez que AIDE peut la détecter

```
[mew@dock ~]$ sudo aide --check
Entry /etc/ssh/sshd_config.d in databases has different attributes: 30020001d b0020081d
Entry /etc/ssh/sshd_config.d/50-redhat.conf in databases has different attributes: 30020001d b8020081d
Start timestamp: 2024-01-12 16:34:47 +0100 (AIDE 0.16)
AIDE found differences between database and filesystem!!

Summary:
  Total number of entries:      37647
  Added entries:                0
  Removed entries:              0
  Changed entries:              2

---------------------------------------------------
Changed entries:
---------------------------------------------------

f   ...    .C... : /etc/aide.conf
f   ...    .C... : /etc/chrony.conf

---------------------------------------------------
Detailed information about changes:
---------------------------------------------------

File: /etc/aide.conf
  SHA512   : FuQFXyO377TOwHVb/jQVM0dxRYbNdDBL | MwDqjbvJtU2E/y+VVMWKMND6448GgI91
             btQhKsF4xN/E5wwLIBIYdTiu5lcFsVbl | u1V7dmsQbWGrroaSThIKrM5sOmrO8WGn
             WcLQL/L0Omjuca1Zh3EHNQ==         | lBh//WyXEpvVIotEv0pAJw==

File: /etc/chrony.conf
  SHA512   : mxnL0LwnC6zYv6OhbZIDGk4I77CViet9 | 8HpCPAGMyiRMszkgLsL/Oue/DZWIcKg6
             OuvkEftOx6//0q/C+2IumzKNS3ZwaD+J | WJbTImBOrPB0omLeev+SSz2+FJZqkGMU
             vzi1SgC6kqWBm97LFaaJXw==         | m/zoWqHajuSW3+gQ8q9XxQ==


---------------------------------------------------
The attributes of the (uncompressed) database(s):
---------------------------------------------------

/var/lib/aide/aide.db.gz
  MD5      : Vs+zOfx+SC+QpZZxtv/9xg==
  SHA1     : SjLITItP4wBAVRtdLwpzrnQBzWA=
  RMD160   : IrvxgMiMqWc0G4LleDtyi3xOVI8=
  TIGER    : Gx2fz+rsEoUmhjc0nBJhNu8TWR2OYoM4
  SHA256   : KKLEPctmn/W7MeK/Wri1JzKA0PYpRwRG
             IQ1Z8L8j5Mk=
  SHA512   : dCxY7RdLWpbziBziLTt5S6vgTTQIihLV
             G1ACjhg4d1AdCcX3wGBtQS8r2aiMxjf8
             ZV8jS7M0+KA+96hDn8e7Og==


End timestamp: 2024-01-12 16:35:05 +0100 (run time: 0m 18s)
```

🌞 **Timer et service systemd**

- créez un service systemd qui exécute un check AIDE
  - il faut créer un fichier `.service` dans le dossier `/etc/systemd/system/`
     
    [Fichier .service](./Ressource/aide-service.txt)
    
- créez un timer systemd qui exécute un check AIDE toutes les 10 minutes
  - il faut créer un fichier `.timer` dans le dossier `/etc/systemd/system/`
  - il doit porter le même nom que le service, genre `aide.service` et `aide.timer`
  - c'est complètement irréaliste 10 minutes, mais ça vous permettra de faire des tests (vous pouvez même raccourcir encore)
      
     [Fichier .timer](./Ressource/aide-timer.txt)