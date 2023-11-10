# 전산물리학1 18강

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('sample.txt')
col = ['red', 'blue']
mar = ['o', '*']

i = 0
for column in data.T:
    plt.plot(data[:,0], column, color=col[i], marker=mar[i])
    i+=1

plt.show()