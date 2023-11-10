# 전산물리학1 22강

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


fig = plt.figure(figsize=(10,5))
axis = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='3d')

n = 50

x = np.linspace(-3., 3., n)
y = np.linspace(-3., 3., n)

X, Y = np.meshgrid(x, y)
Z = np.sinc(np.sqrt(X**2 + Y**2))

p = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
axis.set_xlabel('x-axis', size=15)
axis.set_ylabel('y-axis', size=15)
axis.set_zlabel('z-axis', size=15)

fig.colorbar(p, shrink=0.5)

plt.show()