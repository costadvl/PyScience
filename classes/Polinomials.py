import numpy as numpy

class Polinomials:
    def __init__(self,coefficients):
        self.coeff = coefficients

    def __call__(self,x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        # Start with the longest list
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(len(other.coeff[:])):
                result_coeff[i] += self.coeff[i]
        return Polinomials(result_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c)-1
        N = len(d)-1
        result_coeff = numpy.zeros(M+N+1)
        for i in range(0,M-1):
            for j in range(0,N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polinomials(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        for i in range(1,len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
            del self.coeff[-1]

    def derivative(self):
        """Copy the polynomial and return its derivative"""
        dpdx = Polinomials(self.coeff[:])
        dpdx.differentiate()
        return dpdx