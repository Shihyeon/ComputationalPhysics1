# 전산물리학1 20강

import numpy as np
import matplotlib.pyplot as plt


# ----------[양방향막대]----------

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)

plt.barh(X, A)
plt.barh(X, [-value for value in B])
# plt.show()


# ----------[양방향막대(ver.for)]----------

Pop = [[5., 30., 45., 22.],
       [5., 25., 50., 20.]]

X = range(4)
Y = []

for i in range(2):
    if(i == 1):
        for value in Pop[i]:
            Y.append(-value)
            plt.barh(X, Pop[i])


# ----------[삼중분할막대(ver.반복구문삭제)]----------

data = np.array([[5., 30., 45., 22.],
                 [5., 25., 50., 20.],
                 [1., 2., 1., 1.]])

color_list = ['blue', 'green', 'orange']

X = np.arange(data.shape[1])
for i in range(data.shape[0]):
    S = np.sum(data[:i], axis=0)    # axis=0는 low를 더하는 것이고, axis=1은 column을 더하는 것
    plt.bar(X, data[i], bottom=S, color=color_list[i%len(color_list)])
plt.show()