# 전산물리학1 17강

import csv
import matplotlib.pyplot as plt

X, Y = [], []

file = open('sample.csv', 'r', encoding='utf-8-sig')

reader = csv.reader(file)

for line in reader:
    values = [float(s) for s in line.split()]
    X.append(values[0])
    Y.append(values[1])

plt.plot(X, Y, 'bo-')
plt.show()