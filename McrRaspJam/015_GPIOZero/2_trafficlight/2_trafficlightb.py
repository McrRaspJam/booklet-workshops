from gpiozero import LED, Button
from time import sleep

led_red = LED(18)
led_amber = LED(15)
led_green = LED(14)
button = Button(2)

while True:
	#Cars on Green
	led_green.on()
	
	button.wait_for_press()
	sleep(3)

	#cars stop
	led_green.off()
	led_amber.on()
	sleep(1)
	led_amber.off()
	led_red.on()
	sleep(1)

	#pedestrians go
	led_green.blink(on_time = 0.5, off_time = 0.5)
	sleep(5)

	#Cars start again
	led_green.off()
	sleep(1)
	
	led_amber.on()
	sleep(1)
	led_red.off()
	led_amber.off()
