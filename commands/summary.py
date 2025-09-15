import csv
import os
from collections import Counter
from rich.console import Console
from rich.table import Table

console = Console()

def summary():
    hosts_path = os.path.join("data", "mock_hosts.csv")
    racks_path = os.path.join("data", "mock_racks.csv")
    switches_path = os.path.join("data", "mock_switches.csv")

    # --- Hosts Summary ---
    if os.path.exists(hosts_path):
        with open(hosts_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            statuses = Counter(row["Status"] for row in reader if row["Status"])

        if statuses:
            table = Table(title="Hosts by Status", show_header=True, header_style="bold magenta")
            table.add_column("Status", style="cyan")
            table.add_column("Count", style="green")

            status_colors = {
                "Available": "green",
                "Pending": "yellow",
                "Reserved": "blue",
                "Scrapped": "red",
            }

            for status, count in statuses.items():
                status_colored = f"[{status_colors.get(status, 'white')}]{status}[/{status_colors.get(status, 'white')}]"
                table.add_row(status_colored, str(count))

            console.print(table)
        else:
            console.print("[yellow]⚠️ No host data found[/yellow]")

    # --- Racks Summary ---
    if os.path.exists(racks_path):
        with open(racks_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            racks_count = sum(1 for _ in reader)

        table = Table(title="Racks Summary", show_header=False)
        table.add_row("Total Racks", str(racks_count))
        console.print(table)
    else:
        console.print("[yellow]⚠️ No rack data found[/yellow]")

    # --- Switches Summary ---
    if os.path.exists(switches_path):
        with open(switches_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            models = Counter(row["Switchmodel"] for row in reader if row["Switchmodel"])

        if models:
            table = Table(title="Switches by Model", show_header=True, header_style="bold magenta")
            table.add_column("Model", style="cyan")
            table.add_column("Count", style="green")

            for model, count in models.items():
                table.add_row(model, str(count))

            console.print(table)
        else:
            console.print("[yellow]⚠️ No switch data found[/yellow]")

