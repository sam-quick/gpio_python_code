#!/usr/bin/python

import os
from time import sleep #import sleep from the time library
import RPi.GPIO as GPIO #import GPIO library

GPIO.setmode(GPIO.BCM) #set pin numbering system to BCM

GPIO.setup(22, GPIO.OUT) #Buzzer
GPIO.setup(27, GPIO.OUT) #LED

loop_count = 0

def morse_s():
    count = 0
    while count < 3: 
        #Dot Dot Dot
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        print(".", end = " ")
        sleep(.1)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        sleep(.1)
        count += 1

def morse_o():
    count = 0
    while count < 3:
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        print("-", end = " ")
        sleep(.2)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        sleep(.2)
        count += 1

def morse_full():
    morse_s()
    morse_o()
    morse_s()
    sleep(1)
    print("")

os.system('clear')
print("Morse Code ...---...")

loop_count = int(input("Times to send SOS: "))

while loop_count > 0:
    loop_count -= 1

    morse_full()

GPIO.cleanup()