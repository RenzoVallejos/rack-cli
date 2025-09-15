import csv
import os
from rich.console import Console
from rich.table import Table

console = Console()

def lookup_host(asset_id):
    if not asset_id:
        console.print("[red]❌ Please provide an asset ID using --asset-id[/red]")
        return

    csv_path = os.path.join("data", "mock_hosts.csv")
    if not os.path.exists(csv_path):
        console.print(f"[red]❌ CSV file not found:[/red] {csv_path}")
        return

    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["AssetId"] == asset_id:
                table = Table(title=f"Host Details for {asset_id}", show_header=False)

                # Status color mapping
                status_colors = {
                    "Available": "green",
                    "Pending": "yellow",
                    "Reserved": "blue",
                    "Scrapped": "red",
                }

                for key, value in row.items():
                    if key == "Status":
                        value = f"[{status_colors.get(value, 'white')}]{value}[/{status_colors.get(value, 'white')}]"
                    table.add_row(key, str(value))

                console.print(table)
                return

    console.print(f"[yellow]⚠️ Asset ID '{asset_id}' not found[/yellow]")

