from scapy.all import *
import random
import time


target_ip = "192.168.1.184"

# Range of ports to scan
port_range = range(20, 1024)

# Perform the slow port scan
def slow_port_scan(ip, ports):
    for port in ports:
        # Create a TCP SYN packet
        syn_packet = IP(dst=ip) / TCP(dport=port, flags="S")

        # Send the packet and receive response
        response = sr1(syn_packet, timeout=1, verbose=0)

        # Check if the port is open
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
            print(f"Port {port} is open")
            # Send RST to close the connection
            rst_packet = IP(dst=ip) / TCP(dport=port, flags="R")
            send(rst_packet, verbose=0)
        elif response and response.haslayer(TCP) and response[TCP].flags == 0x14:
            print(f"Port {port} is closed")
        else:
            print(f"Port {port} is filtered or dropped")
 
        # Introduce a random delay between packets to avoid detection
        delay = random.uniform(0.5, 2.5)
        time.sleep(delay)

# Run the scan
slow_port_scan(target_ip, port_range)
