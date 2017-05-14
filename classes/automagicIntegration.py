"""
the computation technique for integration is the 
Trapezoidal rule with n intervals (n+1)
"""
def trapezoidal(f,a,x,n):
    h = (x-a)/float(n)
    I = 0.5*f(a)
    for i in range(0,n):
        I += f(a+i*h)
    I += 0.5*f(x)
    I *= h
    return I

class Integral:
    def __init__(self,f,a,n=100):
        self.f,self.a,self.n = f,a,n

    def __call__(self,x):
        # this is an example of a wrapper,
        # between trapezoidal function and the class
        return trapezoidal

from math import sin, pi

G = Integral(sin,0,200)
value = G(2*pi)
