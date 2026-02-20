from scapy.all import *

ports = [25,80,53,443,445,8080,8443]

def UDPScan(host):
    print(f"Scanning UDP ports on {host}")

    #Send UDP Packets to each port
    ans, unans = sr(IP(dst=host)/UDP(dports=ports), timeout=3, verbose=0)
    
    #Track which ports got ICMP unreachable
    closed = set()
    for sent, received in ans:
        if received.haslayer(ICMP) and received[ICMP].type == 3 and received[ICMP].code == 3:
            original = received[ICMP].payload

            if original.haslayer(UDP):
                closed.add(original[UDP].dport)
    
    for port in ports:
        if port in closed:
            continue
        else:
            udp_response = False
            
            for sent, received in ans:
                if received.haslayer(UDP) and sent[UDP].dport == port:
                    udp_response = True
                    break
            
            if udp_response:
                print(f"[+] UDP port {port} is open (received response)")
            else:
                print(f"[?] UDP port {port} is open|filtered (no response)"
        