import csv
import os
from rich.console import Console
from rich.table import Table

console = Console()

def list_hosts(
    status=None, platform=None, hostname=None,
    usagetype=None, location=None, checkout_owner=None,
    search_all=None
):
    csv_path = os.path.join("data", "mock_hosts.csv")
    if not os.path.exists(csv_path):
        console.print(f"[red]❌ CSV file not found:[/red] {csv_path}")
        return

    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []

        for row in reader:
            # Apply filters
            if status and row['Status'].lower() != status.lower():
                continue
            if platform and platform.lower() not in row['Platform'].lower():
                continue
            if hostname and hostname.lower() not in row['Hostname'].lower():
                continue
            if usagetype and usagetype.lower() not in row['Usage Type'].lower():
                continue
            if location and location.lower() not in row['Location'].lower():
                continue
            if checkout_owner and checkout_owner.lower() not in row['Checkout Owner'].lower():
                continue
            if search_all:
                if not any(search_all.lower() in str(v).lower() for v in row.values()):
                    continue
            rows.append(row)

    if not rows:
        console.print("[yellow]⚠️ No hosts found with given filters[/yellow]")
        return

    # Color mapping for Status
    status_colors = {
        "Available": "green",
        "Pending": "yellow",
        "Reserved": "blue",
        "Scrapped": "red",
    }

    # Build pretty table
    table = Table(show_header=True, header_style="bold magenta")
    columns = ["AssetId", "Hostname", "Status", "Platform", "Usage Type", "Location", "Checkout Owner"]

    for col in columns:
        table.add_column(col, style="cyan")

    for row in rows:
        status_value = row["Status"]
        status_colored = f"[{status_colors.get(status_value, 'white')}]{status_value}[/{status_colors.get(status_value, 'white')}]"
        table.add_row(
            row["AssetId"],
            row["Hostname"],
            status_colored,
            row["Platform"],
            row["Usage Type"],
            row["Location"],
            row["Checkout Owner"],
        )

    console.print(table)

