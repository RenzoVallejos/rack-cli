import csv
import os
from rich.console import Console
from rich.table import Table

console = Console()

def list_switches():
    csv_path = os.path.join("data", "mock_switches.csv")
    if not os.path.exists(csv_path):
        console.print(f"[red]❌ CSV file not found:[/red] {csv_path}")
        return

    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    if not rows:
        console.print("[yellow]⚠️ No switches found[/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    columns = ["Asset ID", "Name", "Switchmodel", "Associated Racks", "Port Count", "Speed", "Location"]

    for col in columns:
        table.add_column(col, style="cyan")

    for row in rows:
        table.add_row(
            row.get("Asset ID", ""),
            row.get("Name", ""),
            row.get("Switchmodel", ""),
            row.get("Associated Racks", ""),
            row.get("Port Count", ""),
            row.get("Speed", ""),
            row.get("Location", ""),
        )

    console.print(table)

