import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
API_KEY = os.getenv("API_KEY", "mock-secret-token")


def get_hosts(status=None, platform=None, hostname=None,
              usagetype=None, location=None,
              checkout_owner=None, search_all=False):
    """
    Fetch hosts from the API.
    Currently, mock_api.py does not support filters,
    so we just return everything and filter locally.
    """
    headers = {"x-api-key": API_KEY}
    response = requests.get(f"{API_BASE_URL}/hosts", headers=headers)
    response.raise_for_status()
    data = response.json()

    # Optional local filtering (mocked)
    if status:
        data = [h for h in data if h.get("status") == status]
    if platform:
        data = [h for h in data if h.get("platform") == platform]
    if hostname:
        data = [h for h in data if hostname in h.get("hostname", "")]

    return data

def get_racks(location=None, rack_type=None, lab=None, usage=None, search_all=False):
    headers = {"x-api-key": API_KEY}
    response = requests.get(f"{API_BASE_URL}/racks", headers=headers)
    response.raise_for_status()
    data = response.json()

    # Basic local filtering (mock)
    if location:
        data = [r for r in data if r.get("location") == location]

    return data

def get_switches(status=None, rack=None, location=None, search_all=False):
    headers = {"x-api-key": API_KEY}
    response = requests.get(f"{API_BASE_URL}/switches", headers=headers)
    response.raise_for_status()
    data = response.json()

    # Basic local filtering (mock)
    if status:
        data = [s for s in data if s.get("status") == status]
    if rack:
        data = [s for s in data if s.get("rack") == rack]

    return data

