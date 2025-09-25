import json
import click
from api_client import get_hosts

def lookup_host(asset_id: str):
    """
    Find a host by asset_id and display its details in pretty JSON format.
    """
    if not asset_id:
        click.echo('{"error": "Please provide an asset ID using --asset-id"}')
        return

    hosts = get_hosts()
    match = next((h for h in hosts if h.get("asset_id") == asset_id), None)

    if match:
        click.echo(json.dumps(match, indent=4))
    else:
        click.echo(f'{{"warning": "Asset ID {asset_id} not found"}}')

