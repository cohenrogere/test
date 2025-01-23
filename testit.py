import numpy as np
import matplotlib.pyplot as pl

a = np.arange(20)
errs = np.random.rand(len(a))*0.7
b = (0.5*a)+errs
print (b)
