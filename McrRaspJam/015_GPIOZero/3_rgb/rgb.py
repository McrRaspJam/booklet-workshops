from gpiozero import RGBLED

led = RGBLED(21, 16, 20)
led.color = (1, 0, 1)
