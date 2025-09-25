import click
from commands.lookup import lookup_host
from commands.list_hosts import list_hosts
from commands.list_racks import list_racks
from commands.list_switches import list_switches
from commands.rack_contents import rack_contents
from commands.summary import summary


@click.group()
@click.version_option("0.1.0")
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
@click.option('--platform', help='Fuzzy search hosts by platform (case-insensitive)')
@click.option('--hostname', help='Fuzzy search hosts by hostname (case-insensitive)')
@click.option('--usagetype', help='Fuzzy search hosts by usage type (case-insensitive)')
@click.option('--location', help='Fuzzy search hosts by location (case-insensitive)')
@click.option('--checkout-owner', help='Fuzzy search hosts by checkout owner (case-insensitive)')
@click.option('--all', 'search_all', help='Fuzzy search across all fields (case-insensitive)')
def list_hosts_cmd(status, platform, hostname, usagetype, location, checkout_owner, search_all):
    """List all hosts (filter by specific fields or search across all with --all)"""
    list_hosts(status, platform, hostname, usagetype, location, checkout_owner, search_all)


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


@cli.command(name="summary")
def summary_cmd():
    """Show a summary of datacenter resources"""
    summary()


if __name__ == "__main__":
    cli()

