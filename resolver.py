from queue import Full
import socket

def ip_to_domain_fun(ip_address):
    try:
        host_info = socket.gethostbyaddr(ip_address)
        return host_info[0] 
    except socket.error as e:
        print(f"Error performing reverse DNS lookup: {e}")