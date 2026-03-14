from scapy.all import IP, ICMP, sr1, TCP
import time

def tr(target):    
    for t in range(1,31):
        packet = IP(dst=target, ttl=t)/TCP(dport=443, flags='S')
        start = time.time()
        reply = sr1(packet, timeout=0.5, verbose=0)
        end = time.time()
        
        if reply is None:
            print(f"{t}  *  Request timed out")

        else:
            hop_ip = reply.src
            rtt = (end-start)*1000

            print(f"{t}  {hop_ip}  {round(rtt, 2)} ms")

            # stop when destination reached
            if reply.src == target:
                print("Destination reached")
                return