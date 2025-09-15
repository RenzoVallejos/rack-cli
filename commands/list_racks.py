import csv
import os
from rich.console import Console
from rich.table import Table

console = Console()

def list_racks():
    csv_path = os.path.join("data", "mock_racks.csv")
    if not os.path.exists(csv_path):
        console.print(f"[red]❌ CSV file not found:[/red] {csv_path}")
        return

    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    if not rows:
        console.print("[yellow]⚠️ No racks found[/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    columns = ["Rack ID", "Asset ID", "Location", "Lab", "Type", "Usage", "Hosts"]

    for col in columns:
        table.add_column(col, style="cyan")

    for row in rows:
        table.add_row(
            row.get("Rack ID", ""),
            row.get("Asset ID", ""),
            row.get("Location", ""),
            row.get("Lab", ""),
            row.get("Type", ""),
            row.get("Usage", ""),
            row.get("Hosts", ""),
        )

    console.print(table)

