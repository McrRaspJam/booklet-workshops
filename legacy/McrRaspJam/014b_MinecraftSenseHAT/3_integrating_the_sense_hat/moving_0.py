from sense_hat import SenseHat
from mcpi import minecraft

sense = SenseHat()
mc = minecraft.Minecraft.create()

while True:
    event = sense.stick.wait_for_event()
    print(mc.player.getPos())
