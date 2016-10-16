import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Write your program below

#GPIO pins for controller
Enable = 22
InputA = 16
InputB = 18

GPIO.setup(Enable, GPIO.OUT)
GPIO.setup(InputA, GPIO.OUT)
GPIO.setup(InputB, GPIO.OUT)

print("on")
GPIO.output(InputA, GPIO.LOW)
GPIO.output(InputB, GPIO.HIGH)
GPIO.output(Enable, GPIO.HIGH)

sleep(3)

print("off")
GPIO.output(Enable, GPIO.LOW)

sleep(1)

print("reverse")
GPIO.output(	,	)
GPIO.output(	,	)
GPIO.output(	,	)

sleep(3)

print("off")
GPIO.output(Enable, GPIO.LOW)
GPIO.cleanup()




