import csv
import os
from collections import Counter


def summary():
    hosts_path = os.path.join("data", "mock_hosts.csv")
    racks_path = os.path.join("data", "mock_racks.csv")
    switches_path = os.path.join("data", "mock_switches.csv")

    # --- Hosts Summary ---
    if os.path.exists(hosts_path):
        with open(hosts_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            statuses = Counter(row['Status'] for row in reader if row['Status'])
        print("\nHosts by Status:")
        for status, count in statuses.items():
            print(f"  {status}: {count}")

    # --- Racks Summary ---
    if os.path.exists(racks_path):
        with open(racks_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            racks_count = sum(1 for _ in reader)
        print(f"\nTotal Racks: {racks_count}")

       # --- Switches Summary ---
    if os.path.exists(switches_path):
        with open(switches_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            models = Counter(row['Switchmodel'] for row in reader if row['Switchmodel'])
        print("\nSwitches by Model:")
        for model, count in models.items():
            print(f"  {model}: {count}")

