import numpy as np
import pygame as pg
"""
сделать регулирование количества земли на крестьянина
"""

class State:
    number = 0
    statedict = {}
    statenumberdict = {}
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        State.number += 1
        self.number = State.number
        self.settlements = {}
        self.laws = {'Female_emans':False,'Children_labour':True}
        State.statenumberdict[self.number] = self

        State.statedict[self.name] = self




def existing_goods():
    grain = Goods('Grain')
    fish = Goods('Fish')
    fertilizer = Goods('Fertilizer')
    whool = Goods('Whool')
    fabric = Goods('Fabric')
    return grain, fertilizer, fish, whool, fabric