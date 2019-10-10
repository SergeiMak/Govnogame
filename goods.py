import numpy as np
import pygame as pg
"""
сделать регулирование производительности, плодовитости зерна, рождаемости, и прочего-прочего-прочего - реиграбельность
надо бы сделать что-то типа конструктора всяких херовин. это было б прям вообще круто. тип плавучие в море ядерные станции и так далее
"""

class Goods:
    gddict = {}
    def __init__(self, name):
        self.name = name
        self.prices = {}
        Goods.gddict[self.name] = self


    def howmany(self):
        print(1)




def existing_goods():
    grain = Goods('Grain')
    fish = Goods('Fish')
    fertilizer = Goods('Fertilizer')
    whool = Goods('Whool')
    fabric = Goods('Fabric')
    iron = Goods('Iron')
    return grain, fertilizer, fish, whool, fabric, iron