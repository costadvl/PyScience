class Y2:
    """
    Note: there is no Constructor method,
    Python automatically shoots a empty init method 
    but to access to v0 we first have to declare y2.value()
    """
    def value(self,t,v0=0):
        if v0 is not None:
            self.v0 = v0
        g = 9.81
        try:
            value = self.v0*t-0.5*g*t**2
        except AttributeError:
            msg = 'You cannot call value(t) without first '
            'calling value(t,v0) to set v0'
            raise TypeError(msg)
        return value
