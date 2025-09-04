import csv
import os

def rack_contents(rack_id):
    if not rack_id:
        print("Please provide a rack ID using --rack-id")
        return

    hosts_path = os.path.join("data", "mock_hosts.csv")
    switches_path = os.path.join("data", "mock_switches.csv")

    print(f"\nContents of {rack_id}:\n")

    if os.path.exists(hosts_path):
        with open(hosts_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            hosts = [row for row in reader if rack_id in row.get("Location", "")]
            print("Hosts:")
            for h in hosts:
                print(f"  - {h['AssetId']} {h['Hostname']} ({h['Status']})")

    if os.path.exists(switches_path):
        with open(switches_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            switches = [row for row in reader if row['Associated Racks'] == rack_id]
            print("\nSwitches:")
            for s in switches:
                print(f"  - {s['Asset ID']} {s['Name']} ({s['Status']})")

