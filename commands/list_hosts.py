import click
import json
from api_client import get_hosts  # fetches from mock_api via requests


@click.command()
@click.option("--status", default=None, help="Filter hosts by status")
@click.option("--platform", default=None, help="Filter hosts by platform")
@click.option("--hostname", default=None, help="Filter hosts by hostname")
@click.option("--usagetype", default=None, help="(unused in mock API) Filter hosts by usage type")
@click.option("--location", default=None, help="(unused in mock API) Filter hosts by location")
@click.option("--checkout-owner", default=None, help="(unused in mock API) Filter hosts by checkout owner")
@click.option("--search-all", is_flag=True, help="Search all hosts")
def list_hosts_cmd(status, platform, hostname, usagetype, location, checkout_owner, search_all):
    """CLI entrypoint for listing hosts."""
    list_hosts(status, platform, hostname, usagetype, location, checkout_owner, search_all)


def list_hosts(status=None, platform=None, hostname=None,
               usagetype=None, location=None,
               checkout_owner=None, search_all=False):
    """
    Retrieve and display host information from the API in pretty JSON format.
    """

    hosts = get_hosts(
        status=status,
        platform=platform,
        hostname=hostname,
        usagetype=usagetype,
        location=location,
        checkout_owner=checkout_owner,
        search_all=search_all
    )

    if not hosts:
        click.echo("[]")  # empty JSON array
        return

    # Print as pretty JSON
    click.echo(json.dumps(hosts, indent=4))

