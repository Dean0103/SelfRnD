##
# @package 파이썬 완변 가이드
# 파이썬 완변 가이드 도서 Study
# chap 4.7. 계단 오르내리기
##

# 4장 Test
# @brief 4장 Test
# @author Dean
# @date 2019.03.19
# @version 1.0.0
# @details
# 1.
# 2.
# 3.
# 4.
# 변수명 | 설명
# ------- | -------
##

# 계단 오르기 walk에 random으로 누적
# import random
#
# position = 0
# walk = [position]
# steps = 1000
# for i in range(steps):
#     step = 1 if random.randint(0,1) else -1
#     position += step
#     walk.append(position)
#
# print(str(walk[:10]))

# 기술통계 계산과 요약
from pandas import DataFrame, Series
import numpy as np

df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
               index=['a','b','c','d'], columns=['one','two'])

print(df)
# print(df.sum())
# print(df.sum(axis=1))
# print(df.sum(axis=1,skipna=False))
print(df.describe()) # 기술 통계

obj = Series(['a','a','b','c'] * 4)
print(obj.describe())

# DataFrame(walk[:10]).plot(kind='barh')
# plt.show()



