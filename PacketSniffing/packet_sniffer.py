from scapy.all import sniff, IP, TCP, UDP
from colorama import Fore, Style
from collections import Counter
import datetime
import os

# Find PWD and create file path
md_file = os.path.join(os.path.dirname(__file__), "packet_log.md")
# Counts packets per IP
packet_counter = Counter()

# Will store packets
packet_log = []
# Translate protocol IDs to names
protocol_map = {6: "TCP", 17:'UDP', 1: 'ICMP'}

def packet_callback(packet):
    
    # Looka t only IP packets
    if IP in packet:
        # Get the details
        src = packet[IP].src
        dst = packet[IP].dst
        proto = protocol_map.get(packet[IP].proto, str(packet[IP].proto))

        # Ports if TCP/UDP
        if proto == 'TCP' or proto == 'UDP':
            sport = packet.sport
            dport = packet.dport
            port_info = f"{sport} -> {dport}"
        else:
        # Default port if not found
            port_info = "-"
            
        packet_counter[src] += 1
        
        # Print info
        print(f"{Fore.CYAN}Packet detected{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Source IP:{Style.RESET_ALL} {src}")
        print(f"{Fore.GREEN}Destination IP:{Style.RESET_ALL} {dst}")
        print(f"{Fore.YELLOW}Protocol:{Style.RESET_ALL} {proto}")
        print(f"{Fore.MAGENTA}Port:{Style.RESET_ALL} {port_info}")
        print(f"{Fore.BLUE}Total packets from {src}:{Style.RESET_ALL} {packet_counter[src]}")
        print("-" * 50)
        
        # Log packet
        packet_log.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "src_ip": src,
            "dst_ip": dst,
            "protocol": proto,
            "port": port_info,
            "total_from_src": packet_counter[src]
        })

# Stop filter for mac        
def stop_sniff(pkt):
    return False


# Begin sniffing
print("Starting packet capture. Press CTRL+C to stop.")

try:
    # prn - call function, dont store in memory, allow the filter to end it
    sniff(prn=packet_callback, store=False, stop_filter=stop_sniff)
finally:
    
    # Save all the data to an MD file.
    print(f"{Fore.RED}\nCapture stopped by user.{Style.RESET_ALL}")
    # Save log to .MD file
    with open(md_file, "w") as f:
        f.write("| Timestamp | Source IP | Destination IP | Protocol | Port | Total from Source |\n")
        for pkt in packet_log:
            f.write(f"| {pkt['timestamp']} | {pkt['src_ip']} | {pkt['dst_ip']} | {pkt['protocol']} | {pkt['port']} | {pkt['total_from_src']} |\n")
    print(f"{Fore.GREEN}Packet log saved to {"packet_log.md"}{Style.RESET_ALL}")