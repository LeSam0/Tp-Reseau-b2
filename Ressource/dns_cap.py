from scapy.all import sniff

def print_it_please(packet):
    print(f"addresse : {packet['DNS'].summary()}")

sniff(filter="udp and port 53", prn=print_it_please, count=2)
