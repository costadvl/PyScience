import numpy as np

class FuncWithDerivatives:
    def __init__(self, h=1.0E-5):
        self.h = h

    def __call__(self, x):
        raise NotImplementedError\
            ('__call__ missing class {}'.format(self.__class__.__name__))

    def df(self,x):
        """return the first derivative of self.f."""
        h = self.h
        return (self(x+h) - self(x-h)/2.0*h)

    def ddf(self,x):
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)

class MyFunc(FuncWithDerivatives):
    def __init__(self, a):
        FuncWithDerivatives.__init__(self,h=1.0E-5)
        self.a = a

    def __call__(self,x):
        return np.cos(self.a*x)+x**3

    def df(self, x):
        a = self.a
        return -a*np.sin(a*x) + 3*x**2

    def ddf(self, x):
        a = self.a
        return -a*a*np.cos(a*x) + 6*x

class MyComplicatedFunc(FuncWithDerivatives):
    def __init__(self, p, q, r, h=1.0E-5):
        FuncWithDerivatives.__init__(self, h)
        self.p, self.q, self.r = p,q,r

    def __call__(self, x):
        return np.log(abs(self.p*np.tanh(self.q*x*np.cos(self.r*x))))

