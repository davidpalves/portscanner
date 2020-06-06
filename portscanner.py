import socket
import argparse
from time import time

from rich.progress import track
from rich.console import Console

from helpers import validate_port_range, print_result, validate_timeout


class PortScanner():
    def __init__(self):
        self.open_ports = []
        self.console = Console()

    def scan_ports(self, ip_address, port, timeout):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        connection.settimeout(timeout)

        if connection.connect_ex((ip_address, port)) == 0:
            self.open_ports.append(port)
            connection.close()

        return self.open_ports


    def run_scan(self, ip_address, timeout=None, lowest_port=0, highest_port=65535):
        try:
            validate_port_range(lowest_port, highest_port)
            validate_timeout(timeout)
        except Exception as e:
            if hasattr(e, "message"):
                self.console.print(e.message, style="bold red")
            else:
                self.console.print(e, style="bold red")
            return

        start = time()
        for port in track(
            range(lowest_port, highest_port + 1),
            f"[bold yellow]Scanning IP {ip_address}[/bold yellow]",
        ):
            try:
                self.scan_ports(ip_address, port, timeout)
            except socket.gaierror:
                self.console.print(f"[bold red]{ip_address} is an invalid address[/]")
            except KeyboardInterrupt:
                end = time()
                elapsed_time = end - start
                print('\n')
                print_result(ip_address, elapsed_time, self.open_ports)
                return

        end = time()
        elapsed_time = end - start
        print_result(ip_address, elapsed_time, self.open_ports)


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
    scanner = PortScanner()
    scanner.run_scan(
        ip_address=args.url,
        timeout=args.timeout,
        lowest_port=args.lowest_port,
        highest_port=args.highest_port,
    )
