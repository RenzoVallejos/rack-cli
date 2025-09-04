import click
from commands.lookup import lookup_host
from commands.list_hosts import list_hosts
from commands.list_racks import list_racks
from commands.list_switches import list_switches
from commands.rack_contents import rack_contents


@click.group()
def cli():
    """Rack CLI - Manage datacenter host, rack & switch information"""
    pass


@cli.command(name="host")
@click.option('--asset-id', help='Search host by Asset ID')
def lookup_host_cmd(asset_id):
    """Look up a host by Asset ID"""
    lookup_host(asset_id)


@cli.command(name="hosts")
@click.option('--status', help='Filter hosts by status (Available, Reserved, etc.)')
def list_hosts_cmd(status):
    """List all hosts (optionally filter by status)"""
    list_hosts(status)


@cli.command(name="racks")
def list_racks_cmd():
    """List all racks"""
    list_racks()


@cli.command(name="switches")
def list_switches_cmd():
    """List all switches"""
    list_switches()


@cli.command(name="rack-contents")
@click.option('--rack-id', help='Show all hosts and switches in a rack')
def rack_contents_cmd(rack_id):
    """Show hosts & switches in a given rack"""
    rack_contents(rack_id)


if __name__ == "__main__":
    cli()

