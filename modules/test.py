import sys
modulefolder = './interest'
sys.path.insert(0,modulefolder)
from interest import days

for i in range(1,15):
    years = days(1,2,i)/365.0
    print('years',years)

print(sys.path)