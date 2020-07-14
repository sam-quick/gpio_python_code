#!/usr/bin/python

from time import sleep #import sleep from the time library
import RPi.GPIO as GPIO #import GPIO library

GPIO.setmode(GPIO.BCM) #set pin numbering system to BCM

GPIO.setup(17, GPIO.OUT) #set GPIO17 as an output (LED)
GPIO.setup(27, GPIO.OUT) #set GPIO27 as an output (LED)

x = 0

while x < 4:
    print "Lights ON"
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    sleep(1)

    print "Lights OFF"
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    sleep(1)

    x += 1

GPIO.cleanup()