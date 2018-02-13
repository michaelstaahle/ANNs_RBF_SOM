import numpy as np 
import math

class ClassName():
    """docstring for ClassName"""
    def __init__(self, data):
        self.data = data
        self.W = None

    def init_W(self, mu=0, var=1):
        self.W = np.random.normal(mu, var, len(self.data[0]))

    def parse_data(self):
        T = np.empty(len(self.data))
        X = np.empty((len(self.data[1]), len(self.data)))
        for idx, elm in enumerate(self.data):
            T[idx] = elm[2]
            X[0][idx] = elm[0]
            X[1][idx] = elm[1]
            X[2][idx] = 1
        
        return T, X

    def targets(self,interval,span=[0,2*math.pi]):
        x = np.arange(span[1],span[2],interval)
        sinx = np.sin(x)
        sqx = np.sign(sinx)

        return (x, sinx, sqx)
