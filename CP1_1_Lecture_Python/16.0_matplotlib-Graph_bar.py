# 전산물리학1 16강

import matplotlib.pyplot as plt

x = range(0, 20)

y = [v**2 for v in x]

plt.bar(x, y, width=0.7)
plt.title('Histogram')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()