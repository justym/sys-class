#coding:utf-8
import RPi.GPIO as GPIO
import time

#macro
button = 25

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("push button")
count = 0
while True:
    btn = GPIO.input(button)
    if btn == True:
        print("pushed")
        break
    
    time.sleep(1)
    

#clean up
GPIO.cleanup()

#Set Pin into 3.3v and Pin22
