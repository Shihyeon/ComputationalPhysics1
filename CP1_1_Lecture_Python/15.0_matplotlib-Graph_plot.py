# 전산물리학1 15강

import matplotlib.pyplot as plt

X = range(-100, 100)    # -100부터 100-1까지의 정수값을 출력. 즉, 집합 X. (X = [-100, -99, ..., 98, 99])

Y = [x**2 for x in X]    # 집합 X의 원소 x에 대해 집합 Y에 대응

plt.plot(X, Y)
plt.title('Y-X Graph', size=20, color='blue', alpha=1)    # alpha가 구간 [0, 1]일 때 1에 가까우면 불투명, 0에 가까우면 투명하다.
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(-110, 110)
plt.ylim(-500, 10500)
plt.show()