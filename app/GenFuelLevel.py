#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def convert_distance_to_litre():

    # set Trigger to HIGH (ON)
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW (OFF)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # time.time() returns the time in second since the epoch. For linux epoch is (January 1, 1970, 00:00:00 (UTC))
    # Save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    if distance > 0 and distance < 1000:
        #Calculating the amount of fuel in the external tank. Formula: distance in cm x 100 Liters / 8.8cm
        #Each 100 litres for this specific tank is equivalent to 8.8cm
        litre = (distance * 100) / 8.8
        GPIO.cleanup()
        return distance, litre
    else:
        distance = -1
        litre = -1
        return distance, litre