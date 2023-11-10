# 전산물리학1 16강

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))    # figure size를 10*5로 설정

x = np.linspace(0, 1, 100)
y = np.cos(np.pi*2*x)**2

plt.plot(x, y)
plt.show()