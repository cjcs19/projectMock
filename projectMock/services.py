# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests
import json
import urllib3

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Funcion principal')

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

def geturlib():    
    """Funcion de llamada a la funcion real. """
    GATEWAY = "http://3.23.61.144:5000/"
    http = urllib3.PoolManager()
    return send_msg(GATEWAY, http, generate_positive_message())


def send_msg(GATEWAY, http, msg):
    statusCode = None
    body = None
    logger.info("Enviando mensaje al gateway...")
    r = http.request('POST', GATEWAY,  headers={'Content-Type':'application/json'}, body=json.dumps(msg))
    logger.info(r.json())
    statusCode = r.status
    if statusCode == 200:
        body = "OK"
        logger.info("[OK]: Mensaje enviado con exito.")
    else:
        body = "FAIL"
        logger.warning("[FAIL]: No se pudo enviar el mensaje...")

def generate_positive_message():
    """Genera un mensaje TP de prueba. 
        @param positive_message:object TP
    """
    return {
        "user": "Cloud Watch",
        "content": "Alert : Proceso 01 afectado"
    }

