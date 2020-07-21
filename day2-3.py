# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:22:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random

while True:
    color=random.randrange(0,9)
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z-1,38,color)
    time.sleep(0.2)
    