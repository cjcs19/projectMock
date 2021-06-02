# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests
import json

# Local imports...
from projectMock.constants import BASE_URL

TODOS_URL = urljoin(BASE_URL, 'todos')


def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None

def get_titles():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response.json()[0]['title']
    else:
        return None

