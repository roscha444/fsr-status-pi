import RPi.GPIO as GPIO
import time
import logging
import api
import os
import util

LAST_MOVEMENT=0
LAST_API_CALL=0

SENSOR_PIN=0
RED_PIN=0
YELLOW_PIN=0
GREEN_PIN=0

def eventRegistered(channel):
    api.setStatusOpen()
    GPIO.output(GREEN_PIN,GPIO.HIGH)
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    global LAST_MOVEMENT
    LAST_MOVEMENT=util.getCurrentTime()

def main():
    global SENSOR_PIN
    global RED_PIN
    global YELLOW_PIN
    global GREEN_PIN
    SENSOR_PIN=int(os.environ.get("SENSOR_PIN"))
    RED_PIN=int(os.environ.get("RED_PIN"))
    YELLOW_PIN=int(os.environ.get("YELLOW_PIN"))
    GREEN_PIN=int(os.environ.get("GREEN_PIN"))
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(YELLOW_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    try:
        logging.info('Register callback for pin: %s', SENSOR_PIN)

        GPIO.output(YELLOW_PIN,GPIO.HIGH)
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)

        GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=eventRegistered)

        while True:
            time.sleep(60)

            global LAST_MOVEMENT
            if(util.timestampIsOlderThanTwoMinutes(LAST_MOVEMENT)):
                logging.info('set status close')
                GPIO.output(RED_PIN,GPIO.HIGH)
                GPIO.output(GREEN_PIN, GPIO.LOW)
                GPIO.output(YELLOW_PIN, GPIO.LOW)
                api.setStatusClose()

    except KeyboardInterrupt:
        logging.info("Close Application...!")
        GPIO.cleanup()
