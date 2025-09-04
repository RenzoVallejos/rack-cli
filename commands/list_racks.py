import csv
import os

def list_racks():
    csv_path = os.path.join("data", "mock_racks.csv")
    if not os.path.exists(csv_path):
        print("CSV file not found:", csv_path)
        return

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("\nAll Racks:\n")
        for row in reader:
            print(f"{row['Rack ID']} - {row['Location']} (Capacity: {row['Capacity']}, Used: {row['UsedSlots']})")

