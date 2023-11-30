from scapy.all import sniff

def print_it_please(packet):
    print(f"""TCP SYN ACK reçu !
- Adresse IP src : {packet['IP'].src}
- Adresse IP dst : {packet['IP'].dst}
- Port TCP src : {packet['TCP'].sport}
- Port TCP dst : {packet['TCP'].dport}""")

sniff(filter="tcp", prn=print_it_please, count=1)
