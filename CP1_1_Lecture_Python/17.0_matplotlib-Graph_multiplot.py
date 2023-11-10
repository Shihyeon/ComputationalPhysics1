# 전산물리학1 17강

import numpy as np
import matplotlib.pyplot as plt

def plot_slope(X, Y):
    dX = X[1:] - X[:-1]
    dY = Y[1:] - Y[:-1]
    plt.plot(X[1:], dY/dX, 'r--')    # 미분계수 설정

x = np.linspace(-3, 3, 100)
y = np.exp(-x**2)

plt.plot(x, y, 'b-')
plot_slope(x, y)    # dy/dx plot
plt.show()