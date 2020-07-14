#!/usr/bin/python

import glob
import os
from time import sleep #import sleep from the time library
import RPi.GPIO as GPIO #import GPIO library

GPIO.setmode(GPIO.BCM) #set pin numbering system to BCM

GPIO.setup(17, GPIO.OUT) #Blue LED
GPIO.setup(27, GPIO.OUT) #Red LED

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():

    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()

    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

temperature = read_temp()

print(str(temperature) + "C") 

if temperature > 21: 
    GPIO.output(27, GPIO.HIGH)
    sleep(5)
    GPIO.output(27, GPIO.LOW)

if temperature < 19:
    GPIO.output(17, GPIO.HIGH)
    sleep(5)
    GPIO.output(17, GPIO.LOW)

GPIO.cleanup()