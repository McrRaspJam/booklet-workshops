from mcpi import minecraft

mc = minecraft.Minecraft.create()

while True:
    for hit in mc.events.pollBlockHits()
        print(hit.pos)
