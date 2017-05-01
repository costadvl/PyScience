import numpy as np
import matplotlib.pylab as pl

def H(x):
    return (0 if x<0 else 1)

x = np.linspace(-2,4,900)
# y = H(x)this won't work since it's an array comparison

#Loop Solution
def H_loop(x):
    r = np.zeros(len(x))
    for i in range(len(x)):
        r[i] = H(x[i])  #inspect's each element and returns the value
    return r

# y = H_loop(x)

#Automatic Vectorization
H_vec = np.vectorize(H) #Not faster than the one above

#   y = H_vec(x)

# Manual Vectorization
def Hv(x):
    return np.where(x < 0, 0.0, 1.0) # 1.0 and 0.0 are meant for array

y = Hv(x)

#ploting-array isues between negative and zero

#The hat function
def Nv(x):
    r = np.where(x<0,0.0,x)
    import operator #since mltiple operator conditions does not work with array arguments
    condition = operator.and_(0<=x,x<1)
    r = np.where(condition,x,r)
    condition = operator.and_(1<=x,x<2)
    r = np.where(condition,2-x,r)
    r = np.where(x>=2,0.0,r)
    print(r)
    return r

def Nv_indexAlternative(x):
    import operator
    r = x.copy()
    r[x<0.0] = 0.0
    condition = operator.and_(0<=x,x<1)
    r[condition] = x[condition]
    condition = operator.and_(1<=x,x<2)
    r[condition] = 2-x[condition]



y2 = Nv(x)
pl.plot(x,y2)
pl.show()
