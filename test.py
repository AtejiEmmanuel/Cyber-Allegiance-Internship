#!/usr/bin/env python3
import socket

def packet_sniffer():
    # Create a raw socket
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    
    # Bind it to the local host
    sniffer.bind(("0.0.0.0", 0))
    
    # Include IP headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    # Receive packets
    print("Sniffing packets... Press Ctrl+C to stop.")
    try:
        while True:
            raw_packet = sniffer.recvfrom(65565)
            print(raw_packet)
    except KeyboardInterrupt:
        print("\nStopping packet sniffer.")
        sniffer.close()

if __name__ == "__main__":
    packet_sniffer()