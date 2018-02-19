import numpy as np 
import math

class annRBF():
    """docstring for ClassName"""
    def __init__(self, data, test_data):
        self.data = data
        self.W = None
        self.phi = None
        self.test_data = test_data 
        self.phi_test = None

#Defines the gaussian-shaped RBF functions/nodes
    def rbf(self, x, mu, sigma2):
        out = np.exp(-((x-mu)**2)/(2*sigma2))
        return out


    def init_W(self, n, mu=0, var=1):
        self.W = np.random.normal(mu, var, n)


    def init_phi(self, X, n, mu, sigma2=1):
        k = len(X)
        self.phi = np.empty((n, k), dtype=float)
        for i in range(n):
            for j in range(k):
                self.phi[i, j] = self.rbf(X[j], mu[i], sigma2)

    def init_phi_test(self, X, n, sigma2=1):
        low = min(X)
        high = max(X)
        mu = np.arange(low, high, (high - low)/n)

        k = len(X)
        self.phi_test = np.empty((n, k), dtype=float)
        for i in range(n):
            for j in range(k):
                self.phi_test[i, j] = self.rbf(X[j], mu[i], sigma2)

# updating the weights incrementally (according to the delta rule) but for all the data points. 
# Not sure what the difference is between incremental and batch in this case.
# We are supose to do both. 

    def total_error(self, Y):
        error = Y - np.dot(self.W, self.phi)
        sum_sqr_error = sum(error**2)
        return error, sum_sqr_error

    def total_error_test(self, Y):
        error = Y - np.dot(self.W, self.phi_test)
        sum_sqr_error = sum(error**2)
        return error, sum_sqr_error

    def update_weights(self, eta):
            for k in range(self.data[0].size):
                delta_w = eta * (self.data[1][k] - np.dot(self.phi[:, k], self.W)) * self.phi[:, k]
                self.W += delta_w


    def fkn_approx(self, epochs, eta, n):
        self.init_W(n)
        low = min(self.data[0])
        high = max(self.data[0])
        mu = np.arange(low, high, (high - low)/n)
        self.init_phi(self.data[0], n, mu)

        for _ in range(epochs):
            self.update_weights(eta)

    def get_approx(self):
        approx_val = np.dot(self.W, self.phi)
        return approx_val  