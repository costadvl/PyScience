from matplotlib.pylab import *
from numpy import *

def f(t):
    return t**2*exp(-t**2)

def f2(t):
    return t**2*f(t)

t = linspace(0,3,51)
y = f(t)
y2 = f2(t)

plot(t, y, 'r-', t, y2, 'bo')
xlabel('The X lable name')
ylable('The Y lable name')
savefig('imagenguardada.png')
show()

