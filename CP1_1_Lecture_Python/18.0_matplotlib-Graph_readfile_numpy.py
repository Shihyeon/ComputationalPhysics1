# 전산물리학1 18강

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('sample.txt')

X = data[:, 0]    # 모든(:) column에 대해 low=0을 출력
Y = data[:, 1]    # 모든(:) column에 대해 low=1을 출력

plt.plot(X, Y, 'bo-')
plt.show()