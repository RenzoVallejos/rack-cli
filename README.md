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
cd /filepath/rack-cli
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip 
install -r requirements.txt #Installs Click and Rich for table formatting
```
## Example commands with images
```bash
# Look up a host by asset ID
python rack_cli.py host --asset-id H1002
  Produces:
               Host Details for H1002              
┌────────────────┬──────────────────────────────┐
│ AssetId        │ H1002                        │
│ HardwareId     │ HW-74203                     │
│ Hostname       │ host-002.mocklab.example.com │
│ Hostclass      │ database                     │
│ Platform       │ x86                          │
│ Manufacturer   │ Lenovo                       │
│ Usage Type     │ Test                         │
│ Status         │ Available                    │
│ InfraStatus    │ Healthy                      │
│ LAN IP         │ 172.25.95.196                │
│ BMC IP         │ 172.23.42.81                 │
│ K2 IP          │ 172.22.243.1                 │
│ State          │ NY                           │
│ Checkout Owner │ diana                        │
│ First Seen     │ 2024-05-27                   │
│ Location       │ DC-West                      │
│ Unnamed: 16    │                              │
└────────────────┴──────────────────────────────┘

# List all hosts
python rack_cli.py hosts
Produces:
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ AssetId ┃ Hostname                     ┃ Status    ┃ Platform ┃ Usage Type ┃ Location ┃ Checkout Owner ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ H1000   │ host-000.mocklab.example.com │ Pending   │ x86      │ Production │ DC-East  │                │
│ H1001   │ host-001.mocklab.example.com │ Scrapped  │ x86      │ Test       │ DC-East  │ diana          │
│ H1002   │ host-002.mocklab.example.com │ Available │ x86      │ Test       │ DC-West  │ diana          │
│ H1003   │ host-003.mocklab.example.com │ Available │ x86      │ Production │ DC-East  │ bob            │
│ H1004   │ host-004.mocklab.example.com │ Available │ x86      │ Test       │ DC-East  │ charlie        │
│ H1005   │ host-005.mocklab.example.com │ Pending   │ ARM      │ Test       │ DC-East  │ bob            │
│ H1006   │ host-006.mocklab.example.com │ Scrapped  │ x86      │ Staging    │ DC-North │ diana          │
│ H1007   │ host-007.mocklab.example.com │ Available │ ARM      │ Test       │ DC-West  │                │
│ H1008   │ host-008.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-North │                │
│ H1009   │ host-009.mocklab.example.com │ Reserved  │ x86      │ Staging    │ DC-East  │ alice          │
│ H1010   │ host-010.mocklab.example.com │ Reserved  │ x86      │ Test       │ DC-West  │ diana          │
│ H1011   │ host-011.mocklab.example.com │ Scrapped  │ ARM      │ Staging    │ DC-West  │ charlie        │
│ H1012   │ host-012.mocklab.example.com │ Reserved  │ ARM      │ Production │ DC-West  │ diana          │
│ H1013   │ host-013.mocklab.example.com │ Pending   │ ARM      │ Production │ DC-North │ bob            │
│ H1014   │ host-014.mocklab.example.com │ Scrapped  │ x86      │ Production │ DC-North │ alice          │
│ H1015   │ host-015.mocklab.example.com │ Reserved  │ x86      │ Test       │ DC-North │ bob            │
│ H1016   │ host-016.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-West  │ bob            │
│ H1017   │ host-017.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │                │
│ H1018   │ host-018.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ diana          │
│ H1019   │ host-019.mocklab.example.com │ Pending   │ x86      │ Staging    │ DC-West  │ alice          │
│ H1020   │ host-020.mocklab.example.com │ Scrapped  │ ARM      │ Staging    │ DC-West  │ bob            │
│ H1021   │ host-021.mocklab.example.com │ Scrapped  │ ARM      │ Production │ DC-North │ diana          │
│ H1022   │ host-022.mocklab.example.com │ Scrapped  │ ARM      │ Production │ DC-West  │ charlie        │
│ H1023   │ host-023.mocklab.example.com │ Reserved  │ ARM      │ Staging    │ DC-West  │ bob            │
│ H1024   │ host-024.mocklab.example.com │ Available │ ARM      │ Production │ DC-North │                │
│ H1025   │ host-025.mocklab.example.com │ Pending   │ x86      │ Test       │ DC-North │ alice          │
│ H1026   │ host-026.mocklab.example.com │ Pending   │ ARM      │ Production │ DC-East  │ diana          │
│ H1027   │ host-027.mocklab.example.com │ Available │ x86      │ Production │ DC-North │ alice          │
│ H1028   │ host-028.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-West  │ diana          │
│ H1029   │ host-029.mocklab.example.com │ Scrapped  │ ARM      │ Test       │ DC-North │ diana          │
│ H1030   │ host-030.mocklab.example.com │ Scrapped  │ x86      │ Production │ DC-East  │ bob            │
│ H1031   │ host-031.mocklab.example.com │ Pending   │ x86      │ Staging    │ DC-East  │ bob            │
│ H1032   │ host-032.mocklab.example.com │ Scrapped  │ ARM      │ Staging    │ DC-East  │ charlie        │
│ H1033   │ host-033.mocklab.example.com │ Available │ ARM      │ Test       │ DC-West  │ charlie        │
│ H1034   │ host-034.mocklab.example.com │ Scrapped  │ x86      │ Production │ DC-East  │                │
│ H1035   │ host-035.mocklab.example.com │ Scrapped  │ x86      │ Staging    │ DC-West  │ diana          │
│ H1036   │ host-036.mocklab.example.com │ Reserved  │ ARM      │ Test       │ DC-East  │                │
│ H1037   │ host-037.mocklab.example.com │ Available │ x86      │ Test       │ DC-North │ charlie        │
│ H1038   │ host-038.mocklab.example.com │ Pending   │ ARM      │ Test       │ DC-North │ charlie        │
│ H1039   │ host-039.mocklab.example.com │ Scrapped  │ x86      │ Test       │ DC-West  │                │
│ H1040   │ host-040.mocklab.example.com │ Reserved  │ ARM      │ Production │ DC-East  │ bob            │
│ H1041   │ host-041.mocklab.example.com │ Reserved  │ x86      │ Staging    │ DC-North │ diana          │
│ H1042   │ host-042.mocklab.example.com │ Pending   │ ARM      │ Staging    │ DC-East  │ alice          │
│ H1043   │ host-043.mocklab.example.com │ Available │ x86      │ Production │ DC-East  │ charlie        │
│ H1044   │ host-044.mocklab.example.com │ Available │ x86      │ Production │ DC-West  │ diana          │
│ H1045   │ host-045.mocklab.example.com │ Reserved  │ ARM      │ Staging    │ DC-East  │ alice          │
│ H1046   │ host-046.mocklab.example.com │ Pending   │ ARM      │ Production │ DC-West  │                │
│ H1047   │ host-047.mocklab.example.com │ Pending   │ ARM      │ Staging    │ DC-North │                │
│ H1048   │ host-048.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ alice          │
│ H1049   │ host-049.mocklab.example.com │ Available │ x86      │ Staging    │ DC-East  │ diana          │
└─────────┴──────────────────────────────┴───────────┴──────────┴────────────┴──────────┴────────────────┘

# Filter by status (case-insensitive)
python rack_cli.py hosts --status available
Produces: 
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ AssetId ┃ Hostname                     ┃ Status    ┃ Platform ┃ Usage Type ┃ Location ┃ Checkout Owner ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ H1002   │ host-002.mocklab.example.com │ Available │ x86      │ Test       │ DC-West  │ diana          │
│ H1003   │ host-003.mocklab.example.com │ Available │ x86      │ Production │ DC-East  │ bob            │
│ H1004   │ host-004.mocklab.example.com │ Available │ x86      │ Test       │ DC-East  │ charlie        │
│ H1007   │ host-007.mocklab.example.com │ Available │ ARM      │ Test       │ DC-West  │                │
│ H1008   │ host-008.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-North │                │
│ H1016   │ host-016.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-West  │ bob            │
│ H1017   │ host-017.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │                │
│ H1018   │ host-018.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ diana          │
│ H1024   │ host-024.mocklab.example.com │ Available │ ARM      │ Production │ DC-North │                │
│ H1027   │ host-027.mocklab.example.com │ Available │ x86      │ Production │ DC-North │ alice          │
│ H1028   │ host-028.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-West  │ diana          │
│ H1033   │ host-033.mocklab.example.com │ Available │ ARM      │ Test       │ DC-West  │ charlie        │
│ H1037   │ host-037.mocklab.example.com │ Available │ x86      │ Test       │ DC-North │ charlie        │
│ H1043   │ host-043.mocklab.example.com │ Available │ x86      │ Production │ DC-East  │ charlie        │
│ H1044   │ host-044.mocklab.example.com │ Available │ x86      │ Production │ DC-West  │ diana          │
│ H1048   │ host-048.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ alice          │
│ H1049   │ host-049.mocklab.example.com │ Available │ x86      │ Staging    │ DC-East  │ diana          │
└─────────┴──────────────────────────────┴───────────┴──────────┴────────────┴──────────┴────────────────┘

# Fuzzy filter by platform
python rack_cli.py hosts --platform x86
Produces:
┃ AssetId ┃ Hostname                     ┃ Status    ┃ Platform ┃ Usage Type ┃ Location ┃ Checkout Owner ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ H1000   │ host-000.mocklab.example.com │ Pending   │ x86      │ Production │ DC-East  │                │
│ H1001   │ host-001.mocklab.example.com │ Scrapped  │ x86      │ Test       │ DC-East  │ diana          │
│ H1002   │ host-002.mocklab.example.com │ Available │ x86      │ Test       │ DC-West  │ diana          │
│ H1003   │ host-003.mocklab.example.com │ Available │ x86      │ Production │ DC-East  │ bob            │
│ H1004   │ host-004.mocklab.example.com │ Available │ x86      │ Test       │ DC-East  │ charlie        │
│ H1006   │ host-006.mocklab.example.com │ Scrapped  │ x86      │ Staging    │ DC-North │ diana          │
│ H1009   │ host-009.mocklab.example.com │ Reserved  │ x86      │ Staging    │ DC-East  │ alice          │
│ H1010   │ host-010.mocklab.example.com │ Reserved  │ x86      │ Test       │ DC-West  │ diana          │
│ H1014   │ host-014.mocklab.example.com │ Scrapped  │ x86      │ Production │ DC-North │ alice          │
│ H1015   │ host-015.mocklab.example.com │ Reserved  │ x86      │ Test       │ DC-North │ bob            │
│ H1017   │ host-017.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │                │
│ H1018   │ host-018.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ diana          │
│ H1019   │ host-019.mocklab.example.com │ Pending   │ x86      │ Staging    │ DC-West  │ alice          │
│ H1025   │ host-025.mocklab.example.com │ Pending   │ x86      │ Test       │ DC-North │ alice          │
│ H1027   │ host-027.mocklab.example.com │ Available │ x86      │ Production │ DC-North │ alice          │
│ H1030   │ host-030.mocklab.example.com │ Scrapped  │ x86      │ Production │ DC-East  │ bob            │
│ H1031   │ host-031.mocklab.example.com │ Pending   │ x86      │ Staging    │ DC-East  │ bob            │
│ H1034   │ host-034.mocklab.example.com │ Scrapped  │ x86      │ Production │ DC-East  │                │
│ H1035   │ host-035.mocklab.example.com │ Scrapped  │ x86      │ Staging    │ DC-West  │ diana          │
│ H1037   │ host-037.mocklab.example.com │ Available │ x86      │ Test       │ DC-North │ charlie        │
│ H1039   │ host-039.mocklab.example.com │ Scrapped  │ x86      │ Test       │ DC-West  │                │
│ H1041   │ host-041.mocklab.example.com │ Reserved  │ x86      │ Staging    │ DC-North │ diana          │
│ H1043   │ host-043.mocklab.example.com │ Available │ x86      │ Production │ DC-East  │ charlie        │
│ H1044   │ host-044.mocklab.example.com │ Available │ x86      │ Production │ DC-West  │ diana          │
│ H1048   │ host-048.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ alice          │
│ H1049   │ host-049.mocklab.example.com │ Available │ x86      │ Staging    │ DC-East  │ diana          │

# Global fuzzy search across all fields
python rack_cli.py hosts --all west 
# This will perform a case-insensitive fuzzy match across all host fields and return any entries containing "west".
Produces:
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ AssetId ┃ Hostname                     ┃ Status    ┃ Platform ┃ Usage Type ┃ Location ┃ Checkout Owner ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ H1002   │ host-002.mocklab.example.com │ Available │ x86      │ Test       │ DC-West  │ diana          │
│ H1007   │ host-007.mocklab.example.com │ Available │ ARM      │ Test       │ DC-West  │                │
│ H1010   │ host-010.mocklab.example.com │ Reserved  │ x86      │ Test       │ DC-West  │ diana          │
│ H1011   │ host-011.mocklab.example.com │ Scrapped  │ ARM      │ Staging    │ DC-West  │ charlie        │
│ H1012   │ host-012.mocklab.example.com │ Reserved  │ ARM      │ Production │ DC-West  │ diana          │
│ H1016   │ host-016.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-West  │ bob            │
│ H1017   │ host-017.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │                │
│ H1018   │ host-018.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ diana          │
│ H1019   │ host-019.mocklab.example.com │ Pending   │ x86      │ Staging    │ DC-West  │ alice          │
│ H1020   │ host-020.mocklab.example.com │ Scrapped  │ ARM      │ Staging    │ DC-West  │ bob            │
│ H1022   │ host-022.mocklab.example.com │ Scrapped  │ ARM      │ Production │ DC-West  │ charlie        │
│ H1023   │ host-023.mocklab.example.com │ Reserved  │ ARM      │ Staging    │ DC-West  │ bob            │
│ H1028   │ host-028.mocklab.example.com │ Available │ ARM      │ Staging    │ DC-West  │ diana          │
│ H1033   │ host-033.mocklab.example.com │ Available │ ARM      │ Test       │ DC-West  │ charlie        │
│ H1035   │ host-035.mocklab.example.com │ Scrapped  │ x86      │ Staging    │ DC-West  │ diana          │
│ H1039   │ host-039.mocklab.example.com │ Scrapped  │ x86      │ Test       │ DC-West  │                │
│ H1044   │ host-044.mocklab.example.com │ Available │ x86      │ Production │ DC-West  │ diana          │
│ H1046   │ host-046.mocklab.example.com │ Pending   │ ARM      │ Production │ DC-West  │                │
│ H1048   │ host-048.mocklab.example.com │ Available │ x86      │ Staging    │ DC-West  │ alice          │
└─────────┴──────────────────────────────┴───────────┴──────────┴────────────┴──────────┴────────────────┘

# List racks
python rack_cli.py racks
Produces:
┏━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
┃ Rack ID  ┃ Asset ID ┃ Location ┃ Lab   ┃ Type     ┃ Usage      ┃ Hosts ┃
┡━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
│ Rack-001 │ H1000    │ DC-North │ Lab-3 │ Standard │ Storage    │ 28    │
│ Rack-002 │ H1001    │ DC-East  │ Lab-4 │ Network  │ Compute    │ 31    │
│ Rack-003 │ H1002    │ DC-East  │ Lab-4 │ Standard │ Compute    │ 7     │
│ Rack-004 │ H1003    │ DC-North │ Lab-5 │ Standard │ Storage    │ 9     │
│ Rack-005 │ H1004    │ DC-East  │ Lab-3 │ Network  │ Compute    │ 32    │
│ Rack-006 │ H1005    │ DC-North │ Lab-3 │ Standard │ Storage    │ 39    │
│ Rack-007 │ H1006    │ DC-North │ Lab-1 │ Network  │ Networking │ 20    │
│ Rack-008 │ H1007    │ DC-West  │ Lab-3 │ Blade    │ Compute    │ 40    │
│ Rack-009 │ H1008    │ DC-West  │ Lab-4 │ Blade    │ Networking │ 24    │
│ Rack-010 │ H1009    │ DC-East  │ Lab-5 │ Standard │ Storage    │ 10    │
│ Rack-011 │ H1010    │ DC-East  │ Lab-2 │ Standard │ Networking │ 27    │
│ Rack-012 │ H1011    │ DC-North │ Lab-4 │ Network  │ Compute    │ 21    │
│ Rack-013 │ H1012    │ DC-West  │ Lab-5 │ Blade    │ Compute    │ 34    │
│ Rack-014 │ H1013    │ DC-North │ Lab-3 │ Blade    │ Compute    │ 39    │
│ Rack-015 │ H1014    │ DC-East  │ Lab-4 │ Standard │ Compute    │ 39    │
│ Rack-016 │ H1015    │ DC-North │ Lab-2 │ Standard │ Storage    │ 5     │
│ Rack-017 │ H1016    │ DC-West  │ Lab-1 │ Blade    │ Networking │ 27    │
│ Rack-018 │ H1017    │ DC-West  │ Lab-1 │ Network  │ Storage    │ 35    │
│ Rack-019 │ H1018    │ DC-North │ Lab-5 │ Network  │ Compute    │ 32    │
│ Rack-020 │ H1019    │ DC-West  │ Lab-4 │ Network  │ Compute    │ 39    │
│ Rack-021 │ H1020    │ DC-North │ Lab-2 │ Blade    │ Networking │ 14    │
│ Rack-022 │ H1021    │ DC-North │ Lab-2 │ Standard │ Compute    │ 37    │
│ Rack-023 │ H1022    │ DC-West  │ Lab-3 │ Blade    │ Storage    │ 11    │
│ Rack-024 │ H1023    │ DC-West  │ Lab-5 │ Standard │ Networking │ 38    │
│ Rack-025 │ H1024    │ DC-West  │ Lab-2 │ Standard │ Compute    │ 20    │
│ Rack-026 │ H1025    │ DC-North │ Lab-1 │ Network  │ Storage    │ 37    │
│ Rack-027 │ H1026    │ DC-North │ Lab-3 │ Network  │ Storage    │ 6     │
│ Rack-028 │ H1027    │ DC-East  │ Lab-5 │ Standard │ Compute    │ 37    │
│ Rack-029 │ H1028    │ DC-West  │ Lab-1 │ Blade    │ Compute    │ 17    │
│ Rack-030 │ H1029    │ DC-North │ Lab-5 │ Standard │ Storage    │ 27    │
│ Rack-031 │ H1030    │ DC-North │ Lab-4 │ Network  │ Storage    │ 31    │
│ Rack-032 │ H1031    │ DC-West  │ Lab-1 │ Network  │ Compute    │ 35    │
│ Rack-033 │ H1032    │ DC-North │ Lab-1 │ Network  │ Networking │ 20    │
│ Rack-034 │ H1033    │ DC-East  │ Lab-4 │ Standard │ Networking │ 36    │
│ Rack-035 │ H1034    │ DC-North │ Lab-1 │ Network  │ Networking │ 19    │
│ Rack-036 │ H1035    │ DC-East  │ Lab-5 │ Network  │ Networking │ 12    │
│ Rack-037 │ H1036    │ DC-North │ Lab-1 │ Blade    │ Networking │ 15    │
│ Rack-038 │ H1037    │ DC-East  │ Lab-2 │ Network  │ Networking │ 32    │
│ Rack-039 │ H1038    │ DC-West  │ Lab-5 │ Standard │ Compute    │ 21    │
│ Rack-040 │ H1039    │ DC-West  │ Lab-2 │ Standard │ Networking │ 39    │
│ Rack-041 │ H1040    │ DC-West  │ Lab-5 │ Blade    │ Networking │ 40    │
│ Rack-042 │ H1041    │ DC-East  │ Lab-4 │ Standard │ Storage    │ 16    │
│ Rack-043 │ H1042    │ DC-East  │ Lab-2 │ Standard │ Networking │ 38    │
│ Rack-044 │ H1043    │ DC-North │ Lab-4 │ Standard │ Networking │ 24    │
│ Rack-045 │ H1044    │ DC-North │ Lab-5 │ Blade    │ Networking │ 27    │
│ Rack-046 │ H1045    │ DC-North │ Lab-1 │ Network  │ Networking │ 11    │
│ Rack-047 │ H1046    │ DC-East  │ Lab-1 │ Blade    │ Storage    │ 36    │
│ Rack-048 │ H1047    │ DC-West  │ Lab-4 │ Network  │ Storage    │ 18    │
│ Rack-049 │ H1048    │ DC-East  │ Lab-4 │ Network  │ Storage    │ 38    │
│ Rack-050 │ H1049    │ DC-East  │ Lab-3 │ Network  │ Storage    │ 8     │
└──────────┴──────────┴──────────┴───────┴──────────┴────────────┴───────┘

# List switches
python rack_cli.py switches
Produces:
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ Asset ID ┃ Name                           ┃ Switchmodel ┃ Associated Racks ┃ Port Count ┃ Speed  ┃ Location ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ S2000    │ switch-001.mocklab.example.com │ Juniper-QFX │ Rack-012         │ 48         │ 40Gbps │ DC-West  │
│ S2001    │ switch-002.mocklab.example.com │ Juniper-QFX │ Rack-006         │ 24         │ 1Gbps  │ DC-East  │
│ S2002    │ switch-003.mocklab.example.com │ Arista-7050 │ Rack-038         │ 24         │ 10Gbps │ DC-West  │
│ S2003    │ switch-004.mocklab.example.com │ Cisco-9300  │ Rack-014         │ 64         │ 1Gbps  │ DC-West  │
│ S2004    │ switch-005.mocklab.example.com │ Arista-7050 │ Rack-002         │ 24         │ 1Gbps  │ DC-West  │
│ S2005    │ switch-006.mocklab.example.com │ Cisco-9300  │ Rack-026         │ 24         │ 40Gbps │ DC-West  │
│ S2006    │ switch-007.mocklab.example.com │ Cisco-9300  │ Rack-020         │ 24         │ 25Gbps │ DC-East  │
│ S2007    │ switch-008.mocklab.example.com │ Arista-7050 │ Rack-028         │ 64         │ 25Gbps │ DC-East  │
│ S2008    │ switch-009.mocklab.example.com │ Arista-7050 │ Rack-020         │ 64         │ 1Gbps  │ DC-North │
│ S2009    │ switch-010.mocklab.example.com │ Juniper-QFX │ Rack-005         │ 48         │ 10Gbps │ DC-West  │
│ S2010    │ switch-011.mocklab.example.com │ Arista-7050 │ Rack-035         │ 64         │ 25Gbps │ DC-West  │
│ S2011    │ switch-012.mocklab.example.com │ Arista-7050 │ Rack-010         │ 64         │ 25Gbps │ DC-North │
│ S2012    │ switch-013.mocklab.example.com │ Cisco-9300  │ Rack-034         │ 24         │ 40Gbps │ DC-North │
│ S2013    │ switch-014.mocklab.example.com │ Juniper-QFX │ Rack-049         │ 64         │ 25Gbps │ DC-West  │
│ S2014    │ switch-015.mocklab.example.com │ Cisco-9300  │ Rack-040         │ 64         │ 10Gbps │ DC-North │
│ S2015    │ switch-016.mocklab.example.com │ Juniper-QFX │ Rack-039         │ 64         │ 10Gbps │ DC-North │
│ S2016    │ switch-017.mocklab.example.com │ Arista-7050 │ Rack-004         │ 48         │ 10Gbps │ DC-North │
│ S2017    │ switch-018.mocklab.example.com │ Cisco-9300  │ Rack-012         │ 48         │ 1Gbps  │ DC-East  │
│ S2018    │ switch-019.mocklab.example.com │ Cisco-9300  │ Rack-012         │ 24         │ 10Gbps │ DC-East  │
│ S2019    │ switch-020.mocklab.example.com │ Arista-7050 │ Rack-048         │ 24         │ 10Gbps │ DC-West  │
│ S2020    │ switch-021.mocklab.example.com │ Arista-7050 │ Rack-046         │ 48         │ 1Gbps  │ DC-West  │
│ S2021    │ switch-022.mocklab.example.com │ Arista-7050 │ Rack-007         │ 64         │ 25Gbps │ DC-North │
│ S2022    │ switch-023.mocklab.example.com │ Cisco-9300  │ Rack-039         │ 64         │ 25Gbps │ DC-North │
│ S2023    │ switch-024.mocklab.example.com │ Arista-7050 │ Rack-027         │ 64         │ 1Gbps  │ DC-West  │
│ S2024    │ switch-025.mocklab.example.com │ Juniper-QFX │ Rack-017         │ 24         │ 25Gbps │ DC-West  │
│ S2025    │ switch-026.mocklab.example.com │ Juniper-QFX │ Rack-047         │ 48         │ 1Gbps  │ DC-East  │
│ S2026    │ switch-027.mocklab.example.com │ Cisco-9300  │ Rack-001         │ 24         │ 25Gbps │ DC-East  │
│ S2027    │ switch-028.mocklab.example.com │ Juniper-QFX │ Rack-019         │ 24         │ 25Gbps │ DC-North │
│ S2028    │ switch-029.mocklab.example.com │ Cisco-9300  │ Rack-050         │ 48         │ 40Gbps │ DC-East  │
│ S2029    │ switch-030.mocklab.example.com │ Juniper-QFX │ Rack-015         │ 64         │ 25Gbps │ DC-East  │
│ S2030    │ switch-031.mocklab.example.com │ Arista-7050 │ Rack-027         │ 48         │ 10Gbps │ DC-East  │
│ S2031    │ switch-032.mocklab.example.com │ Arista-7050 │ Rack-030         │ 24         │ 25Gbps │ DC-East  │
│ S2032    │ switch-033.mocklab.example.com │ Arista-7050 │ Rack-036         │ 48         │ 1Gbps  │ DC-North │
│ S2033    │ switch-034.mocklab.example.com │ Cisco-9300  │ Rack-013         │ 24         │ 10Gbps │ DC-East  │
│ S2034    │ switch-035.mocklab.example.com │ Cisco-9300  │ Rack-011         │ 24         │ 25Gbps │ DC-North │
│ S2035    │ switch-036.mocklab.example.com │ Cisco-9300  │ Rack-023         │ 64         │ 25Gbps │ DC-West  │
│ S2036    │ switch-037.mocklab.example.com │ Juniper-QFX │ Rack-026         │ 48         │ 40Gbps │ DC-West  │
│ S2037    │ switch-038.mocklab.example.com │ Juniper-QFX │ Rack-028         │ 64         │ 40Gbps │ DC-East  │
│ S2038    │ switch-039.mocklab.example.com │ Cisco-9300  │ Rack-049         │ 24         │ 1Gbps  │ DC-West  │
│ S2039    │ switch-040.mocklab.example.com │ Arista-7050 │ Rack-027         │ 48         │ 10Gbps │ DC-West  │
│ S2040    │ switch-041.mocklab.example.com │ Cisco-9300  │ Rack-039         │ 24         │ 40Gbps │ DC-West  │
│ S2041    │ switch-042.mocklab.example.com │ Arista-7050 │ Rack-005         │ 48         │ 25Gbps │ DC-West  │
│ S2042    │ switch-043.mocklab.example.com │ Cisco-9300  │ Rack-019         │ 64         │ 25Gbps │ DC-North │
│ S2043    │ switch-044.mocklab.example.com │ Juniper-QFX │ Rack-013         │ 64         │ 40Gbps │ DC-West  │
│ S2044    │ switch-045.mocklab.example.com │ Juniper-QFX │ Rack-039         │ 64         │ 10Gbps │ DC-East  │
│ S2045    │ switch-046.mocklab.example.com │ Arista-7050 │ Rack-030         │ 64         │ 40Gbps │ DC-North │
│ S2046    │ switch-047.mocklab.example.com │ Cisco-9300  │ Rack-015         │ 48         │ 25Gbps │ DC-West  │
│ S2047    │ switch-048.mocklab.example.com │ Cisco-9300  │ Rack-034         │ 24         │ 25Gbps │ DC-North │
│ S2048    │ switch-049.mocklab.example.com │ Cisco-9300  │ Rack-027         │ 24         │ 1Gbps  │ DC-North │
│ S2049    │ switch-050.mocklab.example.com │ Arista-7050 │ Rack-001         │ 48         │ 40Gbps │ DC-West  │
└──────────┴────────────────────────────────┴─────────────┴──────────────────┴────────────┴────────┴──────────┘

# Show rack contents
python rack_cli.py rack-contents --rack-id Rack-001
Produces:

Contents of Rack Rack-001

                                  Hosts (Location: DC-North)                                   
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ AssetId ┃ Hostname                     ┃ Status    ┃ Platform ┃ Usage Type ┃ Checkout Owner ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ H1006   │ host-006.mocklab.example.com │ Scrapped  │ x86      │ Staging    │ diana          │
│ H1008   │ host-008.mocklab.example.com │ Available │ ARM      │ Staging    │                │
│ H1013   │ host-013.mocklab.example.com │ Pending   │ ARM      │ Production │ bob            │
│ H1014   │ host-014.mocklab.example.com │ Scrapped  │ x86      │ Production │ alice          │
│ H1015   │ host-015.mocklab.example.com │ Reserved  │ x86      │ Test       │ bob            │
│ H1021   │ host-021.mocklab.example.com │ Scrapped  │ ARM      │ Production │ diana          │
│ H1024   │ host-024.mocklab.example.com │ Available │ ARM      │ Production │                │
│ H1025   │ host-025.mocklab.example.com │ Pending   │ x86      │ Test       │ alice          │
│ H1027   │ host-027.mocklab.example.com │ Available │ x86      │ Production │ alice          │
│ H1029   │ host-029.mocklab.example.com │ Scrapped  │ ARM      │ Test       │ diana          │
│ H1037   │ host-037.mocklab.example.com │ Available │ x86      │ Test       │ charlie        │
│ H1038   │ host-038.mocklab.example.com │ Pending   │ ARM      │ Test       │ charlie        │
│ H1041   │ host-041.mocklab.example.com │ Reserved  │ x86      │ Staging    │ diana          │
│ H1047   │ host-047.mocklab.example.com │ Pending   │ ARM      │ Staging    │                │
└─────────┴──────────────────────────────┴───────────┴──────────┴────────────┴────────────────┘
                                    Switches                                     
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┓
┃ Asset ID ┃ Name                           ┃ Switchmodel ┃ Port Count ┃ Speed  ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━┩
│ S2026    │ switch-027.mocklab.example.com │ Cisco-9300  │ 24         │ 25Gbps │
│ S2049    │ switch-050.mocklab.example.com │ Arista-7050 │ 48         │ 40Gbps │
└──────────┴────────────────────────────────┴─────────────┴────────────┴────────┘

# Summary view
python rack_cli.py summary
Produces:

   Hosts by Status   
┏━━━━━━━━━━━┳━━━━━━━┓
┃ Status    ┃ Count ┃
┡━━━━━━━━━━━╇━━━━━━━┩
│ Pending   │ 11    │
│ Scrapped  │ 13    │
│ Available │ 17    │
│ Reserved  │ 9     │
└───────────┴───────┘
   Racks Summary    
┌─────────────┬────┐
│ Total Racks │ 50 │
└─────────────┴────┘
   Switches by Model   
┏━━━━━━━━━━━━━┳━━━━━━━┓
┃ Model       ┃ Count ┃
┡━━━━━━━━━━━━━╇━━━━━━━┩
│ Juniper-QFX │ 13    │
│ Arista-7050 │ 18    │
│ Cisco-9300  │ 19    │
└─────────────┴───────┘

```
