from mcpi import minecraft, block
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlock(x, y + 2, z, block.GRASS.id)
