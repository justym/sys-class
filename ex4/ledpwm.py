#coding: utf-8
import RPi.GPIO as GPIO
import time

#macro
led=24

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

#pwm signal
p = GPIO.PWM(led,1000)

#start of pwm
p.start(0) #duty ratio is 0
for i in range(3):
    for dutyratio in range(0, 101, 10):
        p.ChangeDutyCycle(dutyratio)
        time.sleep(1)
    for dutyration in range(100, -1, -10):
        p.ChangeDutyCycle(dutyratio)
        time.sleep(1)

#clean up
p.stop()
GPIO.cleanup()