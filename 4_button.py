#!/usr/bin/python

import os
from time import sleep #import sleep from the time library
import RPi.GPIO as GPIO #import GPIO library

GPIO.setmode(GPIO.BCM) #set pin numbering system to BCM

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if (GPIO.input(10) == False):
        print("Button Pressed")
        os.system('date')

        print GPIO.input(10)

        sleep(5)
    else:
        os.system('clear')

        print("Waiting on button press")

        sleep(0.1)

