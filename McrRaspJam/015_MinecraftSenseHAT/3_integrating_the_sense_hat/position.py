from mcpi import minecraft

mc = minecraft.Minecraft.create()

while True:
    for hit in mc.events.pollBlockHits()
        text = hit.pos.x + ", " + hit.pos.y + ", " + hit.pos.z
        print(text)
