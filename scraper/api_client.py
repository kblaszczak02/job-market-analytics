import requests
from config.settings import API_URL, REQUEST_TIMEOUT


def fetch_jobs_from_api():
    response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)

    response.raise_for_status()

    return response.json()