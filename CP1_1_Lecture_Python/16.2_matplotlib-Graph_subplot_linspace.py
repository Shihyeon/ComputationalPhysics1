# 전산물리학1 16강

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)    # 0부터 2*pi까지 균일한 간격을 가진 100개의 데이터를 생성
y1 = np.sin(x)
y2 = np.cos(x)


plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title('Sine Function')
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title('Cosine Function')
#plt.show()



i = np.linspace(-5, 5, 100)
j1 = np.sinh(i)
j2 = np.cosh(i)
j3 = np.tanh(i)


plt.subplot(3, 1, 1)
plt.plot(i, j1)
plt.title('Sinh')
plt.subplot(3, 1, 2)
plt.plot(i, j2)
plt.title('Cosh')
plt.subplot(3, 1, 3)
plt.plot(i, j3)
plt.title('Tanh')
plt.show()