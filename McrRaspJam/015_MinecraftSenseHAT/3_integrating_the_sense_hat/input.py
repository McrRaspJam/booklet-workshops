from sense_hat import SenseHat

sense = SenseHat()

while True:
    event = sense.stick.wait_for_event()
    print(event)
