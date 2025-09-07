import csv
import os

def list_hosts(status=None, platform=None, hostname=None, usagetype=None, location=None, checkout_owner=None, search_all=None):
    csv_path = os.path.join("data", "mock_hosts.csv")
    if not os.path.exists(csv_path):
        print("CSV file not found:", csv_path)
        return

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("\nAll Hosts:\n")
        for row in reader:
            # Case-insensitive exact match for status
            if status and row['Status'].lower() != status.lower():
                continue

            # Fuzzy filters (case-insensitive)
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

            # Global fuzzy search across all fields
            if search_all:
                # Check if the search term appears in ANY column value
                match_found = any(
                    search_all.lower() in str(value).lower() for value in row.values()
                )
                if not match_found:
                    continue

            print(f"{row['AssetId']} - {row['Hostname']} "
                  f"({row['Status']}, Platform: {row['Platform']}, "
                  f"Usage: {row['Usage Type']}, Location: {row['Location']}, "
                  f"Owner: {row['Checkout Owner']})")

