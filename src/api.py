import logging
import os
import requests

def getStatus():
    statusUrl = os.environ.get("API_URL") + "/api/v1/status"
    response = requests.get(statusUrl)
    logging.info('GET status')
    return response.json()["open"]

def setStatusOpen():
    statusOpenUrl = os.environ.get("API_URL") + "/api/v1/status/open"
    response = requests.put(statusOpenUrl, json={"apiSecret": "1999"})
    logging.info('PUT status open')
    return response.json()["success"]

def setStatusClose():
    statusOpenUrl = os.environ.get("API_URL") + "/api/v1/status/close"
    response = requests.put(statusOpenUrl, json={"apiSecret": "1999"})
    logging.info('PUT status closed')
    return response.json()["success"]
