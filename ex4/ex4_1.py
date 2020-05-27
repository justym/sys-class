#coding: utf-8
import RPi.GPIO as GPIO
import time

#macro
servo=24

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT, initial=GPIO.LOW)

#pwm signal
p = GPIO.PWM(servo, 50)

#pwm start
p.start(0)

p.ChangeDutyCycle(2.5)
time.sleep(1)

ls = [-90, -45, 0, 45, 90]
for i in range(3):
    for degree in ls:
        dc = 2.5 + (12.0 - 2.5) / 180 * (degree + 90)
        p.ChangeDutyCycle(dc)
        time.sleep(1)
    

p.stop()
GPIO.cleanup()
