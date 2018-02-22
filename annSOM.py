import numpy as np
import math

class annSOM():
    """docstring for ClassName"""
    def __init__(self, data, test_data):
        self.data = data
        self.W = None
        self.grid = None #W is grid[i,j]
        self.test_data = test_data
        self.neighbourhood = None #list of the relevant nodes to be updated


    def wdist(self,weight): #determines the distance between grid point and input, called by winner()
        dist=(self.data[1]-weight).dot(self.data[1]-weight)
        return dist

    def update_weights(self,eta):
        for i in self.neighbourhood:
            delta_w=eta*(self.data[1]-self.grid[i])
            self.grid[i]=self.W+delta_w

    def winner(self, data): #finds the index of the winning point
        mindist=wdist(grid[0])
        minindex=-1
        for i in range(grid.size):
            if wdist(grid[i])<min:
                mindist=wdist(grid[i])
                minindex=i
        return minindex

    def find_neighbours(self,winner,dist):
        nbrs=np.array(winner)
        np.append(nbrs,neighbour) #TODO: add which the neighbour indices are
