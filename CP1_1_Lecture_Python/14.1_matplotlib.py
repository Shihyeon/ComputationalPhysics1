# 전산물리학1 14강

import matplotlib.pyplot as plt

y = (16, 9, 4, 1, 0, 1, 4, 9, 16)

plt.plot(y, 'co--')    # color=c, point=o line=--
# 또는 plt.plot(y, color='cyan', marker='o', linestyle='--', markersize=10, linewidth=2)
plt.title('Figure Title')
plt.ylabel('y-label')
plt.xlabel('x-label')
plt.show()