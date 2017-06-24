import random

def drawBall(hat):
    color = random.choice(hat)
    hat.remove(color)
    return color, hat

def drawBall2(hat):
    index = random.randint(0, len(hat)-1)
    color = hat.pop(index)
    return color, hat

def drawBall3(hat):
    index = random.randint(0, len(hat)-1)
    color = hat[index]
    del hat[index]
    return color, hat

def new_hat():
    colors = 'black','red','blue'
    hat = []
    for color in colors:
        for i in range(4):
            hat.append(color)
    return hat

n = int(input('How many balls are to be drawn? '))
N = int(input('How many experiments? '))

# Run experiments
M = 0 # nº of success
for e in range(N):
    hat = new_hat()
    balls = []
    for i in range(n):
        color, hat = drawBall(hat)
        balls.append(color)
    if balls.count('black') >= 2:
        M += 1

print('probability {}'.format(float(M)/N))
