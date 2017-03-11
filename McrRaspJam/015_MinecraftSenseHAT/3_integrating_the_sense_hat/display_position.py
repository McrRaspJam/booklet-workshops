from sense_hat import SenseHat
from mcpi import minecraft

sense = SenseHat()
mc = minecraft.Minecraft.create()

while True:
    for hit in mc.events.pollBlockHits()
        text = hit.pos.x + ", " + hit.pos.y + ", " + hit.pos.z
        sense.show_text(text)
