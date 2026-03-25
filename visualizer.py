from rich.console import Console
from rich.table import Table

def draw_table(hops):
    table = Table(title="Packet Visualizer")

    table.add_column("TTL", justify="center", style="cyan")
    table.add_column("IP Address", justify="center", style="magenta")
    table.add_column("RTT", justify="center", style="green")
    table.add_column("Location", justify="center", style="yellow")
    
    for hop in hops:
        table.add_row(
            hop["ttl"],
            hop["ip"],
            hop["rtt"],
            hop["location"]
        )

    console = Console()
    console.print(table)