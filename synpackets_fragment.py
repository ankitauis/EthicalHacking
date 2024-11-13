from scapy.all import *


# Define target IP and port
target_ip = "192.168.1.184"
target_port = 80

# Create a SYN packet
syn_packet = IP(dst=target_ip, flags="MF")/TCP(dport=target_port, flags='S')

# Fragment the packet
fragmented_packets = fragment(syn_packet, fragsize=8)  # This creates small fragments

# Send the fragmented packets
send(fragmented_packets)
