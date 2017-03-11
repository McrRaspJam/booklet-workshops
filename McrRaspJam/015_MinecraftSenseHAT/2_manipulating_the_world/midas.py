from mcpi import minecraft, block

mc = minecraft.Minecraft.create()

while True:
    for hit in mc.events.pollBlockHits():
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.GOLD_BLOCK.id)
