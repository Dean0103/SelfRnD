##
# @package 파이썬 머신러닝
# 파이썬 머신러닝 도서
# chap 2.
##

# 2장 Test
# @brief 2장 Test
# @author Dean
# @date 2019.03.22
# @version 1.0.0
# @details
# 1.
# 2.
# 3.
# 4.
# 변수명 | 설명
# ------- | -------
##

# iris data load, 2D 산점도
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df = pd.read_csv('D:\\Dean\\GitHub\\pythonML\\iris.data', header=None)
# print(df.tail())

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
x = df.iloc[0:100, [0, 2]].values
plt.scatter(x[:50, 0], x[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()