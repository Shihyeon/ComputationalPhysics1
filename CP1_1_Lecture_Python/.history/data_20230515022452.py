import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from numpy import genfromtxt

data = genfromtxt('data.csv', delimiter=',', encoding='UTF8')

# 모든(:) column=0에 대해 low=0을 출력
X = data[:, 0]
# 모든(:) column=1에 대해 low=1을 출력
Y = data[:, 1]

# Figure
fig, ax = plt.subplots()
plt.plot(X, Y, 'b.')

# Figure title
plt.title('Scatter Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# figure tick setting
plt.tick_params(axis='x', labelsize=10, direction='in')    # tick setting
plt.tick_params(axis='y', labelsize=10, direction='in')

# Currently, there are no minor ticks,
#   so trying to make them visible would have no effect
ax.yaxis.get_ticklocs(minor=True)     # []
# Initialize minor ticks
ax.minorticks_on()
# Now minor ticks exist and are turned on for both axes
# Turn off x-axis minor ticks
ax.xaxis.set_tick_params(which='minor', bottom=False, direction='in')
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())





plt.show()