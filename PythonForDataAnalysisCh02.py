##
# @package PythonForDataAnalysisBook
# Python for Data Analysis
# chap 02. Test
# 예제 깃허브
# http ://github.com/pydata/pydata-book\
# 문의 메일 : Wesmckinnn@gmail.com

##
# Json 모듈의 Load Test
# @brief Json 모듈을 이용한 file load
# @author Dean
# @date 2019.03.06
# @version 1.0.0
# @details bit.ly의 1.usa.gov 데이터
# 1. example.txt load
# 2. open 시 encoding 적용 필요
##
import json

path = 'D:\\Dean\\GitHub\\pydata-book-2nd-edition\\datasets\\bitly_usagov\\example.txt'
records = [json.loads(line) for line in open(path, encoding='UTF-8')]
print(records[0])


# from collections import defaultdict
# def get_counts2(sequence):
#     counts = defaultdict(int) #init 0
#     for x in sequence:
#         counts[x]+=1
#     return counts
#
# get_counts2(1)

