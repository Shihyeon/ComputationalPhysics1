# 전산물리학1 25강

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5))
x = np.linspace(0.0, 1.0, 300)
for subplot in range(1, 7):
    axis = fig.add_subplot(2, 3, subplot)    # 6개의 subplot을 2*3으로 figure에 배열
    y = np.cos(2*np.pi*x*subplot) + 1
    axis.plot(x, y)
    axis.set_xlabel('time [s]')
    axis.set_ylabel('voltage [mV]')
    axis.set_title('$\cos({0} \pi x)$ + 1'.format(subplot))
fig.tight_layout(pad=1.08)    # subplot의 간격 설정
plt.show()