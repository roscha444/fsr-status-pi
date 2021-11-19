import time

def timestampIsOlderThanTwoMinutes(timestamp):
    return (getCurrentTime() - timestamp) >= 100

def timestampIsOlderThanOneMinute(timestamp):
    return (getCurrentTime() - timestamp) >= 50

def getCurrentTime():
    return int(time.time())