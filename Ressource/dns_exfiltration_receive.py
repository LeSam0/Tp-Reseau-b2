from scapy.all import sniff
import sys

def print_it_please(packet):
   print(f"Message : {packet['DNS'].summary()}")
   sys.exit()

sniff(filter="udp and port 53", prn=print_it_please)