# 전산물리학1 25강

import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure(figsize=(10, 5))

axis_1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axis_2 = fig.add_axes([0.45, 0.6, 0.1, 0.2])

x = np.arange(0, 180, 1)
y = np.cos(2*np.pi*x/180) + 1

axis_1.plot(x, y)
axis_2.plot(x, y)
axis_1.set_xlabel('angle [degree]', fontsize=15)
axis_1.set_ylabel('signal [V]', fontsize=15)
axis_1.set_xticks([0, 45, 90, 135, 180])
axis_1.set_xticklabels(['0', '45', '90', '135', '180'])
axis_1.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
axis_1.set_yticklabels(['0', '0.5', '1.0', '1.5', '2.0'])
axis_2.set_xscale('log')
axis_2.set_xbound(1, 100)
axis_2.set_ybound(0.3, 0.7)
axis_2.grid()

plt.show()