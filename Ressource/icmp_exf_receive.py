from scapy.all import sniff
import sys

def print_it_please(packet):
    if (packet['Padding'] != None) :
        print(f"Message : {packet['Padding'].load.decode()}")
        sys.exit()

sniff(filter="icmp", prn=print_it_please)