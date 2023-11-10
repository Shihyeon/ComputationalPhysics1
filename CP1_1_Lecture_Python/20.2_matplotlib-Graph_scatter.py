# 전산물리학1 20강

import numpy as np
import matplotlib.pyplot as plt

np.random.seed()

N = 150
r = 2*np.random.rand(N)
theta = np.pi*2*np.random.rand(N)
area = 200*r**2
colors = theta

fig = plt.figure(figsize=(7, 7))
fig.add_subplot(projection='polar')
plt.scatter(theta, r, c=colors, s=area, cmap='hsv')
plt.show()