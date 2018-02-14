import numpy as np 
from annRBF import annRBF
import math

#Creates the two functions to be approximated in task 1. Can be moved to different class
def targets(step, span=[0,2*math.pi]):
    x = np.arange(span[0], span[1], step)
    sinx = np.sin(x)
    sqx = np.sign(sinx)
    return x, sinx, sqx

#print(targets(0.1))

x, sinx, sqx = targets(0.1)

data1 = [x, sinx]
data2 = [x, sqx]

#print(data1)
#print(data2)

RBF_net = annRBF(data1)

RBF_net.fkn_approx(50, 0.01, 15)

#print(RBF_net.W)
print(RBF_net.TotalError())