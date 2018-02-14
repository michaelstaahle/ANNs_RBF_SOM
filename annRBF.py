import numpy as np 
import math

class annRBF():
    """docstring for ClassName"""
    def __init__(self, data):
        self.data = data
        self.W = None
        self.phi = None

#Defines the gaussian-shaped RBF functions/nodes
    def rbf(self, x, mu, sigma2):
        out = np.exp(-((x-mu)**2)/(2*sigma2))
        return out


    def init_W(self, n, mu=0, var=1):
        self.W = np.random.normal(mu, var, n)


    def init_phi(self, n, mu, sigma2=1):
        k = len(self.data[0])
        self.phi = np.empty((n, k), dtype=float)
        for i in range(n):
            for j in range(k):
                self.phi[i, j] = self.rbf(self.data[0][j], mu[i], sigma2)


# updating the weights incrementally (according to the delta rule) but for all the data points. 
# Not sure what the difference is between incremental and batch in this case.
# We are supose to do both. 

    def total_error(self):
        error = self.data[1] - np.dot(self.W, self.phi)
        return error

    def update_weights(self, eta):
            for k in range(self.data[0].size):
                delta_w = eta * (self.data[1][k] - np.dot(self.phi[:, k], self.W)) * self.phi[:, k]
                self.W += delta_w


    def fkn_approx(self, epochs, eta, n):
        self.init_W(n)
        low = min(self.data[0])
        high = max(self.data[0])
        mu = np.arange(low, high, (high - low)/n)
        self.init_phi(n, mu)

        for _ in range(epochs):
            self.update_weights(eta)

    def get_approx(self):
        approx_val = np.dot(self.W, self.phi)
        return approx_val  