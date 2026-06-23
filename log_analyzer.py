from scapy.all import rdpcap, IP, TCP

packets = rdpcap("net-2009-12-06-11_59.pcap")

failed_logins = {}

for packet in packets:
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags

        if dst_port == 21 or dst_port == 22 or dst_port == 80:
            if src_ip in failed_logins:
                failed_logins[src_ip] += 1
            else:
                failed_logins[src_ip] = 1

print("Suspicious IPs with repeated connection attempts:")
print("")

for ip, count in failed_logins.items():
    if count > 5:
        print("IP: " + ip + " | Attempts: " + str(count))
