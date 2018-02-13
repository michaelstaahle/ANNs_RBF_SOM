import numpy as np 
import math

class annRBF():
    """docstring for ClassName"""
    def __init__(self, data):
        self.data = data
        self.W = None

    def init_W(self, mu=0, var=1):
        self.W = np.random.normal(mu, var, len(self.data[0]))

    def parse_data(self):
        X = self.data[0]
        T = self.data[1]
        return X, T

    def targets(self,interval,span=[0,2*math.pi]):
        x = np.arange(span[1],span[2],interval)
        sinx = np.sin(x)
        sqx = np.sign(sinx)

        return (x, sinx, sqx)

    def rbf(self, x, mu, sigma2):
        out = np.exp(-((x-mu)**2)/(2*sigma2))
        return out

    def update_weights(self, eta):
        X, T = self.parse_data()
        for elm in X:
             
