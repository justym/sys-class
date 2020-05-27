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

for i in range(3):
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(5)
    time.sleep(1)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    p.ChangeDutyCycle(9.75)
    time.sleep(1)
    p.ChangeDutyCycle(12)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)

p.stop()
GPIO.cleanup()
