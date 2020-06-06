import socket
import argparse

from rich.progress import track
from rich.console import Console

from helpers import validate_port_range, print_result, validate_timeout

open_ports = []
console = Console()


def scan_ports(ip_address, port, timeout):
    socket.setdefaulttimeout(timeout)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    if s.connect_ex((ip_address, port)) == 0:
        open_ports.append(port)
        s.close()

    return open_ports


def run_scan(ip_address, timeout=None, lowest_port=0, highest_port=65535):
    found_ports = []

    try:
        validate_port_range(lowest_port, highest_port)
        validate_timeout(timeout)
    except Exception as e:
        if hasattr(e, "message"):
            console.print(e.message, style="bold red")
        else:
            console.print(e, style="bold red")
        return

    for port in track(
        range(lowest_port, highest_port + 1),
        f"[bold yellow]Scanning IP {ip_address}[/bold yellow]",
    ):
        try:
            found_ports = scan_ports(ip_address, port, timeout)
        except socket.gaierror:
            console.print(f"[bold red]{ip_address} is an invalid address[/]")

    print_result(ip_address, found_ports)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan open ports easily")
    parser.add_argument(
        "--url", "-u", type=str, help="URL to be scanned", required=True
    )
    parser.add_argument(
        "--timeout",
        "-t",
        type=float,
        help="Set connection timeout value (in seconds)",
        required=False,
    )
    parser.add_argument(
        "--lowest-port",
        "-lp",
        type=int,
        required=False,
        default=0,
        help="Define which port (0-65535) should start being scanned",
    )
    parser.add_argument(
        "--highest-port",
        "-hp",
        type=int,
        required=False,
        default=65535,
        help="Define which port (0-65535) should finish being scanned",
    )

    args = parser.parse_args()
    run_scan(
        ip_address=args.url,
        timeout=args.timeout,
        lowest_port=args.lowest_port,
        highest_port=args.highest_port,
    )
