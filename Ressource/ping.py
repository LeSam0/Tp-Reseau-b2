from scapy.all import *

def get_mac(ip): 
    arp_request = ARP(pdst = ip) 
    broadcast = Ether(dst ="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast / arp_request 
    answered_list = srp(arp_request_broadcast, timeout = 5, verbose = False)[0] 
    return answered_list[0][1].hwsrc 

def ping (ipsrc, ipdst):
    ping = ICMP(type=8)

    packet = IP(src=ipsrc, dst=ipdst)

    frame = Ether(src=get_mac(ipsrc), dst=get_mac(ipdst))

    final_frame = frame/packet/ping

    answers, unanswered_packets = srp(final_frame, timeout=10)

    print(f"Pong reçu : {answers[0]}")

   