import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from numpy import genfromtxt

data = genfromtxt('data.csv', delimiter=',', encoding='UTF8')

X = data[:, 0]    # 모든(:) column=0에 대해 low=0을 출력
Y = data[:, 1]    # 모든(:) column=1에 대해 low=1을 출력

fig, ax = plt.subplots()
plt.plot(X, Y, 'b.')

plt.title('Scatter Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.tick_params(axis='x', labelsize=10, direction='in')    # tick setting
plt.tick_params(axis='y', labelsize=10, direction='in')
.yaxis.set_minor_locator(tck.AutoMinorLocator())
a
plt.show()