import csv
import os

def list_switches():
    csv_path = os.path.join("data", "mock_switches.csv")
    if not os.path.exists(csv_path):
        print("CSV file not found:", csv_path)
        return

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("\nAll Switches:\n")
        for row in reader:
            print(f"{row['Asset ID']} - {row['Name']} ({row['Status']})")

