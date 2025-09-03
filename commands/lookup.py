import csv
import os

def lookup_by_asset_id(asset_id):
    if not asset_id:
        print("Please provide an asset ID using --asset-id")
        return

    csv_path = os.path.join("data", "hosts.csv")
    if not os.path.exists(csv_path):
        print("CSV file not found at:", csv_path)
        return

    found = False
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['asset_id'] == asset_id:
                print("\nAsset Found:\n")
                for key, value in row.items():
                    print(f"{key}: {value}")
                found = True
                break

    if not found:
        print(f"Asset ID '{asset_id}' not found.")

