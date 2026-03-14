import argparse

from resolver import ip_to_domain_fun
from tracer import tr
# command for dns
def dns():
    dns = argparse.ArgumentParser(description="a python script for converting ip address to domain name.")
    dns.add_argument("ip_address", type=str, help="this consists of ip address of server")
    args = dns.parse_args()
    print(ip_to_domain_fun(args.ip_address))
    
def pv():
    pac = argparse.ArgumentParser(description="a python script for understanding the route of the packet")
    pac.add_argument("target", type=str, help="this consists of input ip address of the packet")
    args = pac.parse_args()
    tr(args.target)
    
if __name__ == "__main__":
    dns()
    pv()