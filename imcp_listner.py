from scapy.all import *

#  handles and process ICMP packets
def icmp_callback(packet):
    if ICMP in packet and packet[ICMP].type == 8:  # Echo Request
        payload = packet[Raw].load.decode() if Raw in packet else ""
        print(f"Received covert data: '{payload}'")

# Sniffs ICMP packets and  callback 
print("Listening for covert ICMP packets...")
sniff(filter="icmp", prn=icmp_callback)
