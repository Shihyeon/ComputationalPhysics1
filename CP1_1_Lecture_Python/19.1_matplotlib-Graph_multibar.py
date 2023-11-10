# 전산물리학1 19강

import numpy as np
import matplotlib.pyplot as plt


# ----------[이중분할막대]----------

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)

plt.bar(X, A)
plt.bar(X, B, bottom=A)
# plt.show()


# ----------[삼중분할막대(ver.반복구문삭제)]----------

data = np.array([[5., 30., 45., 22.],
                 [5., 25., 50., 20.],
                 [1., 2., 1., 1.]])

color_list = ['blue', 'green', 'orange']

X = np.arange(data.shape[1])
for i in range(data.shape[0]):
    # axis=0는 low를 더하는 것이고, axis=1은 column을 더하는 것
    S = np.sum(data[:i], axis=0)
    plt.bar(X, data[i], bottom=S, color=color_list[i % len(color_list)])
plt.show()
