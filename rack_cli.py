# Import the Click library, which makes it easy to build command-line interfaces
import click

# Import the function we wrote in commands/lookup.py that handles the actual lookup logic
from commands.lookup import lookup_by_asset_id


# Define a "group" of CLI commands.
# A group lets you bundle multiple subcommands (like lookup, list, filter, etc.)
@click.group()
def cli():
    """Rack CLI - Manage datacenter host & switch information"""
    # The docstring above becomes the help text for this command group.
    # Right now, this function doesn’t do anything by itself — it's just a container for subcommands.
    pass


# Define a new subcommand under the `cli` group called "lookup"
@cli.command()
# Add an option (argument) to this command: --asset-id
@click.option('--asset-id', help='Search by asset ID')
def lookup(asset_id):
    """Look up host or switch by asset ID"""
    # When the user runs: python rack_cli.py lookup --asset-id A12345
    # Click parses the command and calls this function, passing asset_id="A12345"
    
    # Here we call the real logic function (from lookup.py) to do the CSV search
    lookup_by_asset_id(asset_id)

if __name__ == "__main__":
    cli()  

