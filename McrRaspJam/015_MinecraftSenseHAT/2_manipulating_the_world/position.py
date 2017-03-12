from mcpi import minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
print(pos)
print(pos.x)
print(pos.y)
print(pos.z)
