import csv
import os

def lookup_host(asset_id):
    if not asset_id:
        print("Please provide an asset ID using --asset-id")
        return

    csv_path = os.path.join("data", "mock_hosts.csv")
    if not os.path.exists(csv_path):
        print("CSV file not found:", csv_path)
        return

    found = False
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['AssetId'] == asset_id:
                print("\nHost Details:\n")
                for key, value in row.items():
                    print(f"{key}: {value}")
                found = True
                break

    if not found:
        print(f"Asset ID '{asset_id}' not found.")

