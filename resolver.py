from queue import Full
import socket

def domain_to_ip_fun(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as e:
        print(f"Error performing DNS lookup: {e}")