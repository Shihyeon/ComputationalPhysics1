# 전산물리학1 21강

import numpy as np
import matplotlib.pyplot as plt


# ----------[Polar Coordinate]----------

X = np.linspace(0, 2*np.pi, 100)
Y = (np.sin(2*X))**2

plt.axes(polar=True)
plt.plot(X, Y, color='coral')
# plt.show()



# ----------[3D Graph-Line]----------

fig_L = plt.figure(figsize=(10,5))
axis_L = fig_L.add_axes([0.1, 0.1, 0.8, 0.8], projection='3d')

t = np.linspace(0., 5., 500)
x = np.cos(np.pi*t)
y = np.sin(np.pi*t)
z = 2*t

axis_L.plot(x, y, z)

axis_L.set_xlabel('x-axis', size=15)
axis_L.set_ylabel('y-axis', size=15)
axis_L.set_zlabel('z-axis', size=15)
axis_L.set_xticks([-1.0, -0.5, 0., 0.5, 1.0])
axis_L.set_yticks([-1.0, -0.5, 0., 0.5, 1.0])
# plt.show()


# ----------[3D Graph-Surface]----------

fig_SF = plt.figure(figsize=(10,5))
axis_SF = fig_SF.add_axes([0.1, 0.1, 0.8, 0.8], projection='3d')

n = 20

i = np.linspace(0., 1., n)    # 미분소 x(i)를 mesh n개로 나눈다. n이 클수록 미분한 것처럼 된다.
j = np.linspace(0., 1., n)

I, J = np.meshgrid(i, j)    # surface를 만들기 위한 구문
K = I**2 - J**2

axis_SF.plot_surface(I, J, K)
axis_SF.set_xlabel('x-axis', size=15)
axis_SF.set_ylabel('y-axis', size=15)
axis_SF.set_zlabel('z-axis', size=15)
axis_SF.set_zticks([-1.0, -0.5, 0., 0.5, 1.0])

axis_SF.view_init(elev=30, azim=70)    # graph view position; 구면좌표계에서 theta는 elev이고, phi는 azim이다. 각의 단위는 도이다.
axis_SF.dist = 10    # graph view position; 구면좌표계에서 반지름에 해당한다.

plt.show()