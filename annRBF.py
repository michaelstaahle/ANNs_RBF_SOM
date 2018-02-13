import numpy as np 
import math

class annRBF():
    """docstring for ClassName"""
    def __init__(self, data):
        self.data = data
        self.W = None
        self.phi = None

    def init_W(self, mu=0, var=1):
        self.W = np.random.normal(mu, var, len(self.data[0]))


    def init_phi(self,n,mu,sigma2=1,k=len(self.data)):
        phi=np.empty((n,k))

        for j in range(k):
            for i in range(n):
                phi[i,j] = self.rbf(x[j], mu[i], sigma2[i])

        return phi



    def parse_data(self):
        X = self.data[0]
        T = self.data[1]
        return X, T

#Creates the two functions to be approximated in task 1. Can be moved to different class
    def targets(self,interval,span=[0,2*math.pi]):
        x = np.arange(span[1],span[2],interval)
        sinx = np.sin(x)
        sqx = np.sign(sinx)

        return (x, sinx, sqx)

#Defines the gaussian-shaped RBF functions/nodes
    def rbf(self, x, mu, sigma2):
        out = np.exp(-((x-mu)**2)/(2*sigma2))
        return out



    def fkn_approx(self, epochs, eta):

        self.init_W()
        low = min(self.data[0])
        high = max(self.data[0])
        mu = np.arange(low, high, (high - low)/n)

        self.init_phi(n,mu)
        targets=data[1]
        for i in range(epochs):
            self.update_weights(eta)

        error=targets-np.dot(self.phi*self.W)
        print("error: " + str(error))




    def update_weights(self, eta):
        X, T = self.parse_data()
        for elm in X:
