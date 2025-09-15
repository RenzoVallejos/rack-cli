import csv
import os
from rich.console import Console
from rich.table import Table

console = Console()

def rack_contents(rack_id):
    if not rack_id:
        console.print("[red]❌ Please provide a rack ID using --rack-id[/red]")
        return

    racks_path = os.path.join("data", "mock_racks.csv")
    hosts_path = os.path.join("data", "mock_hosts.csv")
    switches_path = os.path.join("data", "mock_switches.csv")

    # First, find rack location from rack_id
    rack_location = None
    if os.path.exists(racks_path):
        with open(racks_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row.get("Rack ID") == rack_id:
                    rack_location = row.get("Location")
                    break

    console.print(f"\n[bold magenta]Contents of Rack {rack_id}[/bold magenta]\n")

    # --- Hosts ---
    if rack_location and os.path.exists(hosts_path):
        with open(hosts_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            hosts = [row for row in reader if row.get("Location") == rack_location]

        if hosts:
            table = Table(title=f"Hosts (Location: {rack_location})", show_header=True, header_style="bold cyan")
            columns = ["AssetId", "Hostname", "Status", "Platform", "Usage Type", "Checkout Owner"]

            for col in columns:
                table.add_column(col, style="cyan")

            for h in hosts:
                table.add_row(*(h.get(col, "") for col in columns))

            console.print(table)
        else:
            console.print(f"[yellow]⚠️ No hosts found in rack {rack_id} (Location: {rack_location})[/yellow]")
    else:
        console.print("[yellow]⚠️ Could not determine rack location or no hosts CSV found[/yellow]")

    # --- Switches ---
    if os.path.exists(switches_path):
        with open(switches_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            switches = [row for row in reader if row.get("Associated Racks") == rack_id]

        if switches:
            table = Table(title="Switches", show_header=True, header_style="bold cyan")
            columns = ["Asset ID", "Name", "Switchmodel", "Port Count", "Speed"]

            for col in columns:
                table.add_column(col, style="cyan")

            for s in switches:
                table.add_row(*(s.get(col, "") for col in columns))

            console.print(table)
        else:
            console.print("[yellow]⚠️ No switches found in this rack[/yellow]")

