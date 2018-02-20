import numpy as np 
from annRBF import annRBF
import math
import matplotlib.pyplot as plt



#np.random.seed(50)
#Creates the two functions to be approximated in task 1. Can be moved to different class
def targets(step, span=[0,2*math.pi]):
    x = np.arange(span[0], span[1], step)
    sinx = np.sin(x)
    sqx = np.sign(sinx)
    return x, sinx, sqx

def noisy(data, mean, var):
    noise = np.random.normal(mean,var,len(data))
    out = noise + data
    return out

x, sinx, sqx = targets(0.1)
#Allows a choice about noisy/non-noisy data
noise=True
if noise==True:
    sinx = noisy(sinx, 0, 0.1)
    sqx = noisy(sqx, 0, 0.1)

#print(targets(0.1))
data1 = [x, sinx]
data2 = [x, sqx]

x_test, sinx_test, sqx_test = targets(0.1, span=[0.05, 2*math.pi])

data1_test = [x_test, sinx_test]
data2_test = [x_test, sqx_test]

#print(data1)
#print(data2)

RBF_net = annRBF(data1, data1_test)

RBF_net.fkn_approx(100, 0.01, 4)

print(RBF_net.W)

print(RBF_net.total_error(data1[1]))

RBF_net.init_phi_test(data1_test[0], 4)

print(RBF_net.total_error_test(data1_test[1]))

approx_val = RBF_net.get_approx()



plt.plot(x, sinx)
plt.plot(x, approx_val)
plt.show()