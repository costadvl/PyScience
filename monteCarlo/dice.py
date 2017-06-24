import numpy as np

tryOuts = 100000
eyes = np.random.randint(1,7,(tryOuts,4))
compare = eyes == 6
with6 = np.sum(compare, axis=1)
no_success = sum(with6 >= 2)
Probability = float(no_success)/tryOuts

print(no_success, Probability)
