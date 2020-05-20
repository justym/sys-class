#coding:utf-8
import RPi.GPIO as GPIO
import time

#macro
led = 24
button = 25
assigned_seconds = 10

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#loop
while True:
    btn = GPIO.input(button)
    if btn == True:
        print("turn on")
        GPIO.output(led, 1)
        time.sleep(assigned_seconds)
        GPIO.output(led, 0)
        print("turn off")
        break
    
#clean up
GPIO.cleanup()

#Set Pin into Pin18 and Pin20
