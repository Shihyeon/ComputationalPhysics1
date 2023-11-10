# 전산물리학1 17강

import matplotlib.pyplot as plt

X, Y = [], []

for line in open('sample.txt', 'r'):    # r은 read, 즉 읽기 모드로 open
    values = [float(s) for s in line.split()]    # split을 하여 list형으로 생성
    X.append(values[0])    # value에서 low=0을 집합 X라 하자 (float형으로 생성)
    Y.append(values[1])    # value에서 low=1을 집합 Y라 하자 (float형으로 생성)

plt.plot(X, Y, 'bo-')
plt.show()