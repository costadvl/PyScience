import math as math
"""
Vectors in a Plane
"""
class Vect2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # (a,b)+(c,d) = (a+c,b+d)
        return Vect2D(self.x + other.x,self.y + other.y)

    def __mul__(self, other):
        # (a,b)*(c,d) = ac+bd
        return self.x*other.x + self.y*other.y

    def __abs__(self):
        # ||(a,b)|| = sqrt((a,b)*(a,b))
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '({},{})'.format(self.x,self.y)

    def __ne__(self, other):
        # reuse __eq__ method
        return not self.__eq__(other)

    def __len__(self):
        return abs(self)
