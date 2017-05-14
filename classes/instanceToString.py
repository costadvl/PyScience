class Y:
    def __init__(self):
        self.v0 = 1
        self.g = 9.81

    def __call__(self):
        print(self.v0, self.g)
        return 'Y class has been called'

y = Y()
print(y)

class Y2:
    def __init__(self):
        self.vf = 50

    def __call__(self):
        return self.vf

    def __str__(self):
        return ('this is a custom printable class \
        | defalut:{}').format(self)

y2 = Y2
print(y2)