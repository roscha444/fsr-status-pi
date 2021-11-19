import requests
from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO
import time

load_dotenv()
API_URL = os.environ.get("API_URL")
SENSOR_PIN = os.environ.get("SENSOR_PIN")

global LAST_MOVEMENT
LAST_MOVEMENT=0
global LAST_API_CALL
LAST_API_CALL=0

def getStatus():
    statusUrl = API_URL + "/api/v1/status"
    response = requests.get(statusUrl)
    return response.json()["open"]

def setStatusOpen():    
    statusOpenUrl = API_URL + "/api/v1/status/open"
    response = requests.put(statusOpenUrl)
    return response.json()["success"]

def setStatusClose():    
    statusOpenUrl = API_URL + "/api/v1/status/close"
    response = requests.put(statusOpenUrl, json={"apiSecret": os.environ.get("API_SECRET")})
    return response.json()["success"]

def timestampIsOlderThanTwoMinutes(timestamp):
    return (getCurrentTime() - timestamp) > 100

def timestampIsOlderThanOneMinute(timestamp):
    return (getCurrentTime() - timestamp) > 100

def getCurrentTime():
    return int(time.time())

def eventRegistered(channel):
    if(timestampIsOlderThanOneMinute):
        global LAST_API_CALL
        AST_API_CALL=getCurrentTime()
        setStatusOpen()

    global LAST_MOVEMENT
    LAST_MOVEMENT=getCurrentTime()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=eventRegistered)
    while True:
        time.sleep(60 * 2)

        if(timestampIsOlderThanTwoMinutes(LAST_MOVEMENT)):
            setStatusClose()

except KeyboardInterrupt:
    print("Close Application...!")

GPIO.cleanup()