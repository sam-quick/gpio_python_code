#!/usr/bin/python

import os
from time import sleep #import sleep from the time library
import RPi.GPIO as GPIO #import GPIO library

GPIO.setmode(GPIO.BCM) #set pin numbering system to BCM

GPIO.setup(17, GPIO.OUT) #Blue LED
GPIO.setup(27, GPIO.OUT) #Red LED

led_choice = 0
count = 0

os.system('clear')

print "Which LED to blink?"
print "1: Blue"
print "2: Red"

led_choice = input("Select: ")

if led_choice == 1:
    os.system('clear')
    print "Blue LED"
    count = input("Blink count?: ")
    while count > 0:
        GPIO.output(17, GPIO.HIGH)
        sleep(1)
        GPIO.output(17, GPIO.LOW)
        sleep(1)
        
        count = count - 1

if led_choice == 2:
    os.system('clear')
    print "Red LED"
    count = input("Blink count?: ")
    while count > 0:
        GPIO.output(27, GPIO.HIGH)
        sleep(1)
        GPIO.output(27, GPIO.LOW)
        sleep(1)
        
        count = count - 1   

GPIO.cleanup()