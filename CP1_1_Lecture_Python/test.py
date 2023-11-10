from matplotlib.transforms import Bbox
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0., 5., 100)
y = np.sin(4*x) + np.cos(7*x) + np.sin(x)

box = {'facecolor':'lightgreen', 'alpha':0.5}
arrow = {'facecolor':'navy', 'arrowstyle':'->'}

plt.text(1.6, -.5, 'y=f(x)', size=15, bbox=box)
plt.annotate('', xytext=(2, -.2), xy=(1.5, .5), arrowprops=arrow)
plt.plot(x, y, ls='-', label='y=f(x)')

plt.legend(loc=0)
plt. show()