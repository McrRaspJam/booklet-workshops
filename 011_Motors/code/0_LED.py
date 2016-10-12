import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Write your program below

#GPIO pins for LED
LED = 16
GPIO.setup(LED, GPIO.OUT)

print("on")
GPIO.output(LED, GPIO.HIGH)

sleep(5)

print("off")
GPIO.output(LED, GPIO.LOW)
GPIO.cleanup()
