# 전산물리학1 15강

import matplotlib.pyplot as plt

X = range(-30, 30)

Y1 = [v**2 for v in X]
Y2 = [v**3 for v in X]

plt.subplot(2, 1, 1)    # 2*1인 Matrix에서 1*1에 plot 위치
plt.plot(X, Y1)
plt.subplot(2, 1, 2)    # 2*1인 Matrix에서 2*1에 plot 위치
plt.plot(X, Y2)
plt.show()