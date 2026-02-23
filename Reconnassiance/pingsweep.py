from scapy.all import *
import ipaddress

def ping_sweep(network):
    # Create a list of all IPs in the given CIDR (e.g., "192.168.1.0/24")
    ips = [str(ip) for ip in ipaddress.IPv4Network(network, strict=False)]
    
    # Build packets: ICMP Echo Request
    packets = IP(dst=ips)/ICMP()
    
    # Send and receive
    ans, unans = sr(packets, timeout=2, verbose=0)
    
    print("Live hosts:")
    for sent, received in ans:
        if received.haslayer(ICMP) and received[ICMP].type == 0:
            print(f"  {received[IP].src}")