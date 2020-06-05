from rich.console import Console

console = Console()

def validate_port_range(lowest_port, highest_port):
    if lowest_port < 0:
        raise Exception("The lowest port can't be lower than 0.")
    if lowest_port > highest_port:
        raise Exception("The lowest port can't be higher than the highest port.")
    if lowest_port > 65535:
        raise Exception("The lowest port can't be higher than 65535.")
    if highest_port < 0:
        raise Exception("The highest port can't be lower than 0.")
    if highest_port > 65535:
        raise Exception("The highest port can't be higher than 65535.")

def validate_timeout(timeout):
    if timeout < 0:
        raise Exception("You can't set timeout as a negative value.")


def print_result(ip_address, found_ports=None):
    if not found_ports:
        console.print(f"[bold red]No open ports found in {ip_address}[/]")
    else:
        console.print(
            f"[magenta]The open ports in[/magenta] [reverse cyan]{ip_address}[/reverse cyan][magenta] are:[/magenta]"
        )
        for port in found_ports:
            console.print(f"- {ip_address}:[bold red]{port}[/bold red]")
