# 전산물리학1 25강

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)

grid_size = (5, 2)    # figure를 10*2 조각으로 만드는 것

# plt.subplot2grid(grid_size, (a, b), rowspan=c, colspan=d)    # grid_size 또는 (i, j)로 하여 grid를 만들고, 시작 위치 (a, b)로 크기 c*d로 생성

plt.subplot2grid(grid_size, (0, 0), rowspan=3, colspan=1)
plt.plot(np.sin(2*x), np.cos(.5*x))

plt.subplot2grid(grid_size, (0, 1), rowspan=3, colspan=1)
plt.plot(np.cos(2*x), np.sin(x))

plt.subplot2grid(grid_size, (3, 0), rowspan=2, colspan=2)
plt.plot(np.cos(5*x), np.sin(7*x))

plt.tight_layout(pad=1.08)
plt.show()