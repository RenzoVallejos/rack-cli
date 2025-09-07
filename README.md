# rack-cli

A Python command-line tool for managing datacenter host, rack, and switch information.  
Built with [Click](https://click.palletsprojects.com/) for seamless command organization and extensibility.

## Features
- Look up hosts by Asset ID
- List hosts, racks, and switches
- Fuzzy, case-insensitive filtering by:
  - Status
  - Platform
  - Hostname
  - Usage Type
  - Location
  - Checkout Owner
- Global `--all` search across all fields
- Rack contents: show hosts and switches inside a given rack
- Summary view of datacenter resources (hosts by status, rack count, switches by model)


## Setup
Clone the repo and install Click:
```bash
git clone https://github.com/your-username/rack-cli.git
cd rack-cli
pip install -r requirements.txt #Installs Click
```
## Examples
```bash
# Look up a host by asset ID
python rack_cli.py host --asset-id 8401000103

# List all hosts
python rack_cli.py hosts

# Filter by status (case-insensitive)
python rack_cli.py hosts --status available

# Fuzzy filter by platform
python rack_cli.py hosts --platform x86

# Global fuzzy search across all fields
python rack_cli.py hosts --all west

# List racks
python rack_cli.py racks

# List switches
python rack_cli.py switches

# Show rack contents
python rack_cli.py rack-contents --rack-id Rack-12

# Summary view
python rack_cli.py summary
```
