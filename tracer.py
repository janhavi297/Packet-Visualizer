from geo import ip_to_location
from resolver import domain_to_ip_fun
from scapy.all import IP, sr1, TCP
import time

def tr(target):
    hops = []
    target_ip = domain_to_ip_fun(target)
    for t in range(1,31):
        packet = IP(dst=target_ip, ttl=t)/TCP(dport=443, flags='S')
        start = time.time()
        reply = sr1(packet, timeout=4, verbose=0)
        end = time.time()
        
        if reply is not None:
            ip = reply.src
            rtt = (end-start)*1000
            location = ip_to_location(ip)

            hops.append({
                "ttl": str(t),
                "ip": ip,
                "rtt": str(f"{rtt:.2f} ms"),
                "location": location
            })

            if reply.src == target_ip:
                print("Destination reached")
                return hops
        else:
            hops.append({
                "ttl": str(t),
                "ip": "* * *",
                "rtt": "- - -",
                "location": "Request timed out"
            })