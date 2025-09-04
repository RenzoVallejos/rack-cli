import csv
import os

def list_hosts(status=None):
    csv_path = os.path.join("data", "mock_hosts.csv")
    if not os.path.exists(csv_path):
        print("CSV file not found:", csv_path)
        return

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("\nAll Hosts:\n")
        for row in reader:
            if status and row['Status'] != status:
                continue
            print(f"{row['AssetId']} - {row['Hostname']} ({row['Status']})")

