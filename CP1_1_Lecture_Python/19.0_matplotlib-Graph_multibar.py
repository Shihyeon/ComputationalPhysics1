# 전산물리학1 19강

import matplotlib.pyplot as plt

data = [[5., 25., 50., 20.],    # <- data[0]
        [4., 23., 51., 17.],    # <- data[1]
        [6., 22., 52., 19.]]    # <- data[2]

plt.bar(range(4), data[0], width=0.25, color='orange')
plt.bar([x+0.25 for x in range(4)], data[1], width=0.25, color='green')
plt.bar([x+0.50 for x in range(4)], data[1], width=0.25, color='blue')
plt.show()
