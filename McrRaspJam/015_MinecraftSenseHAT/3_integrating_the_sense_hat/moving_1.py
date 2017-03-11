from sense_hat import SenseHat
from mcpi import minecraft

sense = SenseHat()
mc = minecraft.Minecraft.create()

while True:
    event = sense.stick.wait_for_event()
    pos = mc.player.getPos()

    if event.direction == "up":
        pos.z -= 1
    if event.direction == "down":
        pos.z += 1
    if event.direction == "left":
        pos.x -= 1
    if event.direction == "right":
        pos.x += 1

    print(pos)
