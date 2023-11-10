# 전산물리학1 15강

import matplotlib.pyplot as plt

X = range(0, 4)

Y = [v**2 for v in X]

size = [100, 20, 30, 40]

plt.scatter(x = X, y = Y, s = size, c = 'blue', alpha=0.6)    # Scatter는 분산형 함수값의 사이즈(점의 크기)를 정해주고 출력
plt.title('Scatter Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()