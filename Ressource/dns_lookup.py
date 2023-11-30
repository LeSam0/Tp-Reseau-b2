from scapy.all import DNS, DNSQR, IP, sr1, UDP

def dns_lookup(ipdst, domain_name) :

    dns_req = IP(dst=ipdst) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain_name))
    answer = sr1(dns_req, verbose=0)

    print(f"DNS reçu : {answer[0]}")

dns_lookup("8.8.8.8", "www.ynov.com")