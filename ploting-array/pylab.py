from matplotlib.pylab import *
from numpy import *

def f(t):
    return t**2*exp(-t**2)

def f2(t):
    return t**2*f(t)

t = linspace(0,3,51)
y = f(t)
y2 = f2(t)

subplot(2,1,1)
plot(t, y, 'r-', t, y2, 'bo')
xlabel('The X lable name')
ylabel('The Y lable name')
# savefig('plot-first.png')

subplot(2,1,2)
t3 = t[::4]
y3 = f2(t3)
plot(t, y, 'ro', t3, y3, 'ys')
# savefig('plot-second.png')
show()

