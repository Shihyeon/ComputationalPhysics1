# 전산물리학1 16강

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)    # 0부터 2*pi까지 균일한 간격을 가진 100개의 데이터를 생성
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Function')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()    # grid 설정
plt.show()