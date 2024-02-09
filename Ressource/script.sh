#!/bin/bash

function hardeningssh {
echo Port 6525 >> /etc/ssh/ssh_config
echo PermitRootLogin no >> /etc/ssh/ssh_config
echo AuthenticationMethods publickey >> /etc/ssh/ssh_config
echo PubkeyAuthentication yes >> /etc/ssh/ssh_config
echo DenyUsers root >> /etc/ssh/ssh_config
echo AuthorizedKeysFile      .ssh/authorized_keyst >> /etc/ssh/ssh_config
echo IgnoreRhosts yes >> /etc/ssh/ssh_config
echo HostbasedAuthentication no >> /etc/ssh/ssh_config
echo PasswordAuthentication no >> /etc/ssh/ssh_config
echo PermitEmptyPasswords no >> /etc/ssh/ssh_config
echo Protocol 2 >> /etc/ssh/ssh_config
echo UsePAM no >> /etc/ssh/ssh_config
echo X11Forwarding no >> /etc/ssh/ssh_config
echo ClientAliveInterval 300 >> /etc/ssh/ssh_config
echo ClientAliveCountMax 0 >> /etc/ssh/ssh_config
echo Ciphers aes128-ctr,aes192-ctr,aes256-ctr >> /etc/ssh/ssh_config
echo HostKeyAlgorithms ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-rsa,ssh-dss >> /etc/ssh/ssh_config
echo KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha256 >> /etc/ssh/ssh_config
echo MACs hmac-sha2-256,hmac-sha2-512,hmac-sha1 >> /etc/ssh/ssh_config
sudo systemctl reload sshd
sudo firewall-cmd --zone=public --add-port=6525/tcp --permanent
sudo firewall-cmd --zone=public --remove-port=22/tcp --permanent
sudo firewall-cmd --reload
}

function hardeningnginx {

}


