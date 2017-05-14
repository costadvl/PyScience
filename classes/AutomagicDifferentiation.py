"""
Python f(x) in math impementation, 
whith an object Derivative to resolve the derivate of f(x)
Solution: symbolic mathematics (Maple, Mathematica, SymPy.
    limitations - funtions defined in algorithmic way -> numerical diferentiation is requires
See pag.326 
"""

class Derivative:
    def __init__(self,f,h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self,x):
        f,h = self.f,self.h
        # numerical differentiation
        return (f(x+h)-f(x))/h

from math import sin, cos, pi

df = Derivative(sin)
x = pi
result = df(x)

print(cos(x), result)

def f2(x):
    return 100000*(x-0.9)**2*(x-1.1)**3

df2 = Derivative(f2)
print(df2(2))


# TODO: to be continued with the Newton's method Appendix A.1.9
