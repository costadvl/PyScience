import numpy as np

cDgs = np.array([-30 +i*10 for i in range(3)])  #this dosn't make any diference it's a small array/list
fDgs = 9./5*cDgs+32
table = [[C,F] for C,F in zip(cDgs,fDgs)]
table2 = np.asarray(table)

print(type(cDgs),type(fDgs))
print(table2[1,1],table)
