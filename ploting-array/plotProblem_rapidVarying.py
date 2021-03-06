import numpy as np
import matplotlib.pylab as pl

def f(x):
    r = x.copy()
    r[x==0] = np.exp(1-100)
    return np.sin(1.0/r)

x1 = np.linspace(-3,3,71)   # f(0) sin(1/0) caution! should be excluded
x2 = np.linspace(-1,1,1000)
pl.subplot(2,1,1)
pl.plot(x1,f(x1))
pl.subplot(2,1,2)
pl.plot(x2,f(x2))
pl.show()
