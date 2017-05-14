class Y:
    """
    Mathematical function for the vertical motion of the ball
    
    Methods:
        constructor(v0): set initial velocity ...
    
    Atributes:
        v0: the initial velocity .... 
    """
    def __init__(self,v0):
        self.v0 = v0
        self.g = 9.81

    def value(self,t):
        return self.v0*t-0.5*self.g*t**2


class VelocityProfile:
   def __init__(self,beta,mu0,n,R):
       self.beta, self.mu0, self.n, self.R = beta, mu0, n, R

   def value(self,r):
       beta, mu0, n, R = self.beta, self.mu0, self.n, self.R
       n = float(n)
       v = (beta/(2.0*mu0))**(1/n)*(n/(n+1))*\
           (R**(1+1/n)- r**(1+1/n))
       return v
