import argparse
from tracer import tr

def pv():
    pac = argparse.ArgumentParser(description="A python script for understanding the route of the packet")
    pac.add_argument("target", type=str, help="This consists of input ip address of the packet")
    args = pac.parse_args()
    tr(args.target)
    
if __name__ == "__main__":
    pv()