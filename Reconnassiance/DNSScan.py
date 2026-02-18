from scapy.all import *

ports = [25,80,53,443,445,8080,8443]

def DNSScan(host):
    ans,unans = sr(IP(dst=host)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
    if ans:
        print("DNS Server at %s"%host)