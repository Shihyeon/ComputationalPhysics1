# 전산물리학1 20강

import matplotlib.pyplot as plt

labels = 'Seoul', 'Daejeon', 'Busan', 'Daegu'
data = [5, 25, 50, 20]
explode = (0, .1, 0, 0)    # explode는 케이크 조각처럼 만들 Data를 특출나게 하는 것

plt.title('Population size', size=25)
plt.pie(data, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=180)
plt.show()