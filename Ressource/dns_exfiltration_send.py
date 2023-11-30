from scapy.all import *
from sys import argv

data = argv[2]
ip = argv[1]

dns_req = IP(dst=ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=data))
print(f"DNS send to {ip} with {data}")
send(dns_req)
