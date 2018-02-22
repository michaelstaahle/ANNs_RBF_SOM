import numpy as np
import math

class annSOM():
    """docstring for ClassName"""
    def __init__(self, data, test_data):
        self.data = data
        self.W = None
        self.grid = None
        self.test_data = test_data


    def wdist(self,x):
        dist=(x-self.W).dot(x-self.W)
        return dist

    def update_weights(self,eta):
        delta_w=eta*(self.data[1]-self.W)
        self.W=self.W+delta_w

    def winner(self, data):
        mindist=1000; #kan förmodligen ordnas på ett säkrare sätt
        minindex=-1
        for i in range(grid.size):
            if wdist(x)<min:
                mindist=wdist(x)
                minindex=i
        return minindex

