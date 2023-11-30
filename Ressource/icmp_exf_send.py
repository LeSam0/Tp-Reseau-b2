from scapy.all import IP , ICMP , Padding, send
from sys import argv

data = argv[2]
ip = argv[1]


frame = IP(dst=ip)/ICMP()/Padding(data)
print(f"Ping send to {ip} with {data}")
send(frame)

