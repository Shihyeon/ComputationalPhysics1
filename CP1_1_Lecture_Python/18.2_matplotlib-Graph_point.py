# 전산물리학1 18강

import random
import matplotlib.pyplot as plt

count = 1024

X = [random.random() for i in range(count)]
Y = [random.random() for i in range(count)]

plt.scatter(X, Y)
plt.show()