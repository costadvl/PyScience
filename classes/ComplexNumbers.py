import math as math
"""
Example of a posible Complex class
"""


class Complex:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, (float,int)):
            # this is a weak typing since we automatically change
            # the object type
            other = Complex(other)
        elif not (hasattr(other,'real') and hasattr(other,'imag')):
            raise TypeError('other must have real and imag attr.')
        return Complex(self.real + other.real,
                       self.imag + other.imag)
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (float,int)):
           other = Complex(other)
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __rsub__(self,other):
        if isinstance(other, (float,int)):
            other = Complex(other)
        # other-self is not hte same as self-other
        return other.__sub__(self)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __div__(self, other):
        sri, sii, ori, oii = self.real, self.imag, other.real, other.imag
        r = float(ori**2 + oii**2)
        return Complex((sri*ori+sii*oii)/r, (sii*ori-sri*oii)/r)

    def __abs__(self):
        return math.sqrt(self.real**2+self.imag**2)

    def __neg__(self):
        return Complex(-self.real,-self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self,other):
        return not self.__eq__(other)

    def __str__(self):
        return '({},{})'.format(self.real,self.imag)

    def __repr__(self):
       return 'Complex'+str(self)

    def __pow__(self, power):
        raise NotImplementedError\
            ('self**power is not yest impl. for Complex')

    def _illegal(self,op):
        print('illegal operation "{}" for complex numbers'.format(op))

    def __gt__(self, other): self._illegal('>')
    def __ge__(self, other): self._illegal('>=')
    def __lt__(self, other): self._illegal('<')
    def __le__(self, other): self._illegal('<=')
