import numpy as np
import math

class annSOM():
    """docstring for ClassName"""
    def __init__(self, data, test_data):
        self.data = data
        self.W = None
        self.grid = None #W is grid[i,j]
        self.test_data = test_data
        self.neighbourhood = None


    def wdist(self,weight):
        dist=(self.data[1]-weight).dot(self.data[1]-weight)
        return dist

    def update_weights(self,eta):
        for i in neighbourhood:
            delta_w=eta*(self.data[1]-self.grid[i])
            self.grid[i]=self.W+delta_w

    def winner(self, data):
        mindist=wdist(grid[0])
        minindex=-1
        for i in range(grid.size):
            if wdist(grid[i])<min:
                mindist=wdist(grid[i])
                minindex=i
        return minindex

