#!/usr/bin/python

import RPi.GPIO as GPIO #import GPIO library

GPIO.setmode(GPIO.BCM) #set pin numbering system to BCM

GPIO.setup(17, GPIO.OUT) #set GPIO17 as an ouput (LED)
GPIO.setup(27, GPIO.OUT) #set GPIO27 as an output (LED)

print "Lights OFF"

GPIO.output(17, GPIO.LOW) #set out low, 3v3 is inactive
GPIO.output(27, GPIO.LOW) #set out low, 3v3 is inactive