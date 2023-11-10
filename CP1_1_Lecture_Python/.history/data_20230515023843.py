import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from numpy import genfromtxt
from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter


data = genfromtxt('data.csv', delimiter=',', encoding='UTF8')

## 모든(:) column=0에 대해 low=0을 출력
X = data[:, 0]
## 모든(:) column=1에 대해 low=1을 출력
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

# figure minor tick setting
ax.tick_params(axis='x', which='minor', bottom=True)
ax.tick_params(axis='y', which='minor', left=)
## x값이 5의 배수일 때마다 메인 눈금 표시
ax.xaxis.set_major_locator(MultipleLocator(2)) 
ax.yaxis.set_major_locator(MultipleLocator(2))
## 메인 눈금이 표시될 형식
ax.xaxis.set_major_formatter('{x:.0f}')
ax.yaxis.set_major_formatter('{x:.0f}')  
## 서브 눈금은 x값이 1의 배수인 경우마다 표시
ax.xaxis.set_minor_locator(MultipleLocator(1)) 
ax.yaxis.set_minor_locator(MultipleLocator(1))


# # Currently, there are no minor ticks,
# #   so trying to make them visible would have no effect
# ax.yaxis.get_ticklocs(minor=True)     # []
# # Initialize minor ticks
# ax.minorticks_on()
# # Now minor ticks exist and are turned on for both axes
# # Turn off x-axis minor ticks
# ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
# ax.yaxis.set_minor_locator(tck.AutoMinorLocator())





plt.show()