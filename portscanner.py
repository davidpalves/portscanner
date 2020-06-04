import socket, sys
import argparse
from rich.progress import track
from rich.console import Console


def scan_ports(ip_address):
    console = Console()
    console.print("\n")
    
    open_ports = []
    error = False

    for port in track(range(0, 65535), f"[dim yellow]Scanning IP {ip_address}[/dim yellow]"):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            if s.connect_ex((ip_address, port)) == 0:
                open_ports.append(port)
                s.close()
        except socket.gaierror:
            error=True
            break

    if error:    
        console.print(f"[bold red]{ip_address} is an invalid address[/]")
    elif not open_ports:
        console.print(f"[bold red]No open ports found in {ip_address}[/]")
    else:
        console.print(
            f"[magenta]The open ports in[/magenta] [reverse cyan]{ip_address}[/reverse cyan][magenta] are:[/magenta]"
        )
        for port in open_ports:
            console.print(f"- {ip_address}:[bold red]{port}[/bold red]")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Scan open ports easily")
    parser.add_argument('--url', '-u', type=str, help="URL to be scanned", required=True)

    args = parser.parse_args()
    scan_ports(ip_address=args.url)