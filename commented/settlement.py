import numpy as np
import pygame as pg
import pops
#import state


class Settlement:
    Settl_number = 0
    arry = []
    slovar = dict()


    def __init__(self,state, coordinates, mm, name, serfs,schoolers, facnum = 0, size=1):
        self.size = size
        mm[coordinates] = 2
        self.area = []
        self.area.append([coordinates[0],coordinates[1]])
        self.name = name
        self.rectangle = pg.Rect((coordinates[0]-1,coordinates[1]-1),(3,3))
        self.factories = {}
        self.facnum = facnum
        self.serfs_unemployed = serfs
        #self.schoolers = pops.Pops(self,0,schoolers,1,0,1)
        self.pops = {}

        sumcube = 0
        for w in self.factories:
            sumcube += self.factories[w].gehalt*self.factories[w].gehalt*self.factories[w].gehalt
        self.gehsum = {'Serf':0,'Worker':0}

        self.number = Settlement.Settl_number
        Settlement.Settl_number  += 1
        Settlement.arry.append([self.rectangle,self.number])
        Settlement.slovar[self.name] = self
        self.population = 0
        self.state = state
        state.settlements[self] = self


    def stlpopul(self):
        self.population = 0
        for i in self.pops:
            self.population += i.total_num

    def summakubow(self, pop1):
        sumcube = 0
        for w in self.factories:
            if w.work_type == pop1.strata:
                sumcube += self.factories[w].gehalt*self.factories[w].gehalt*self.factories[w].gehalt * self.factories[w].notfull
            #print(sumcube, 'lpl')
        self.gehsum[pop1.strata.name] = sumcube
        #print(self.gehsum, sumcube)

    def display_inform(self):
        print('Number: {}. Name: {}'.format(self.number, self.name))


    def growth(self, mm):
        if self.population > 5000*self.size:
            self.size  += 1
            mm[self.area] = 2               # max + or min -



    def type_change(self, mm):
        if self.size > 10:
            for i in len(self.area):
                mm[self.area[i]] = 3



