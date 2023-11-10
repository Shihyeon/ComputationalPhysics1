# 전산물리학1 16강

import numpy as np
import matplotlib.pyplot as plt

plt.title('Graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.xticks(np.arange(6), ('0', '1', '2', '3', '4', '5'))    # np.arange는 range와 유사. 각 tick에 대응하는 문자를 대입
plt.yticks([0, 5, 10, 15, 20, 25], ('0', '5', '10', '15', '20', '25'))

plt.tick_params(axis='x', labelsize=10, colors='red')    # tick setting
plt.tick_params(axis='y', labelsize=10, colors='blue')

plt.show()