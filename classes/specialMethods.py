class Y :
    def __init__(self,v0):
        self.v0 = v0
        print(self.v0)
    def __call__(self,t):
        # makes the classs callable
        print(t)
    def isCallable(self):
        # you can check if the object is callable
        return callable(self)

y = Y(10)
y(20)
print(callable(y))
