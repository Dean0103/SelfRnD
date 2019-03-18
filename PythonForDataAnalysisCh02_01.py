##
# @package PythonForDataAnalysisBook
# Python for Data Analysis 도서 Study
# chap 02. Test
# 예제 깃허브 http ://github.com/pydata/pydata-book\ 문의 메일 : Wesmckinnn@gmail.com
# Doxygen 기준 주석 작성

##
# Json 모듈의 Load Test
# @brief Json 모듈을 이용한 file load
# @author Dean
# @date 2019.03.06
# @version 1.0.0
# @details bit.ly의 1.usa.gov 데이터
# 1. example.txt load
# 2. open 시 encoding 적용 필요
# 3. timezone[tz] field 불러오기
# 4. timezone 불러오기
# 변수명 | 설명
# ------- | -------
##

import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from pandas import DataFrame, Series
from collections import Counter
import numpy as np

# 타임존 불러오기
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
        return counts

def get_counts2(sequence):
    counts = defaultdict(int) #init 0
    for x in sequence:
        counts[x]+=1
    return counts

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

path = 'D:\\Dean\\GitHub\\pydata-book-2nd-edition\\datasets\\bitly_usagov\\example.txt'
records = [json.loads(line) for line in open(path, encoding='UTF-8')]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

counts = get_counts(time_zones)
# print("get_counts : " + str(counts['America/New_York']))
# print("time_zones : " + str(time_zones))

a = top_counts(counts)
# print("top_counts() : " + str(a[0:]))

counts = Counter(time_zones)
# print("Counter() : " + str(counts.most_common(10)))

frame = DataFrame(records)
# print("DataFrame : " + str(frame.info()))
# print("frame : ")
# print(frame['tz'][:10])

tz_counts = frame['tz'].value_counts()
# print("tz_counts : " + str(tz_counts[:10]))

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
# print("tz_counts : " + str(tz_counts[:10]))

# 막대 차트 그리기
# %matplotlib inline(jupyter notebook) >> import matplotlib.pyplot as plt 변경
# tz_counts[:10].plot(kind='barh', rot=0)
# plt.show()
# print("frame['a'][1] : " + str(frame['a'][1]))
# print("frame['a'][50] : " + str(frame['a'][50]))
# print("frame['a'][51] : " + str(frame['a'][51]))

# 브라우저 종류 확인 - 첫 번째 문자열 토큰 분리
results = Series([x.split()[0] for x in frame.a.dropna()])
# print("results[:5] : " + str(results[:5]))
# print("results.value_counts()[:8] : " + str(results.value_counts()[:8]))

# agent 값이 없는 경우 제외
cframe = frame[frame.a.notnull()]

# 각 행이 Windows인지 아닌지 검사
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
# print('operating_system[:5] : ' + str(operating_system[:5]))

# 표준시간대와 운영체제를 기준으로 데이터를 그룹핑
by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print('agg_counts[:10] : \n' + str(agg_counts[:10]))

# 전체 표준시간대의 순위
indexer = agg_counts.sum(1).argsort()
print('indexer[:10] : \n' + str(indexer[:10]))

count_subset = agg_counts.take(indexer)[-10:]
print('count_subset : \n' + str(count_subset))

# 그룹별 누적 막대
count_subset.plot(kind='barh', stacked=True)
# plt.show()

# 총합을 1로 정규화
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
plt.show()

# print('[:] : \n' + str())
