import FakeRPi.GPIO as GPIO
import time
import logging
import api
import os
import util

LAST_MOVEMENT=0
LAST_API_CALL=0

def eventRegistered(channel):
    if(util.timestampIsOlderThanOneMinute):
        global LAST_API_CALL
        LAST_API_CALL=util.getCurrentTime()
        api.setStatusOpen()
    global LAST_MOVEMENT
    LAST_MOVEMENT=util.getCurrentTime()

def main():
    SENSOR_PIN=os.environ.get("SENSOR_PIN")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
 
    try:
        logging.info('Register callback for pin: %s', SENSOR_PIN)

        GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=eventRegistered)

        while True:
            time.sleep(60 * 2)

            global LAST_MOVEMENT
            if(util.timestampIsOlderThanTwoMinutes(LAST_MOVEMENT)):
                logging.info('set status close')
                api.setStatusClose()

    except KeyboardInterrupt:
        logging.info("Close Application...!")

    GPIO.cleanup()