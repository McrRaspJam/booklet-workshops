if button.is_pressed == True:
    led_green.off()

button.wait_for_press()
led_green.off()
