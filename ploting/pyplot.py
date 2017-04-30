"""
matplotlib recomend to import the modules 
the folowing way
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2*np.exp(-x**2)

def f2(x):
    return x**2*f(x)

x = np.linspace(0,3,51)
y = f(x)
y2 = f2(x*2)

plt.plot(x,y, 'y-')
plt.legend(['local legend'])
plt.xlabel('the X label')
plt.ylabel('the Y label')
plt.axis([0,3,-0.1,0.6])

plt.plot(x,y2, 'bo')
plt.legend(['local legend'])
plt.xlabel('the X label')
plt.ylabel('the Y label')
plt.axis([0,3,-0.1,0.6])

plt.show()

