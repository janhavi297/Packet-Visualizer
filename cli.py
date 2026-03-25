import argparse
from tracer import tr
from visualizer import draw_table

def pv():
    pac = argparse.ArgumentParser(description="A python script for understanding the route of the packet")
    pac.add_argument("target", type=str, help="This consists of input ip address of the packet")
    args = pac.parse_args()
    hops = tr(args.target)
    draw_table(hops)
    
if __name__ == "__main__":
    pv()
