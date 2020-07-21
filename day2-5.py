# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:13:17 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

username=input('請輸入名字:')
messange=input('輸入訊息:')

mc.postToChat('['+username+']'+messange)