##
# @package API Test
##

# API Test
# @brief API Test
# @author Dean
# @date 2019.03.20
# @version 1.0.0
# @details
# KA4 개발서버 : 10.231.227.155
# port = '7578'
# http://10.231.227.155:7578/help
# 변수명 | 설명
# ------- | -------
##

import requests
import json

# base_url = "http://" + ip + ":" + port
ip = "10.231.227.155"
port = "7578"
base_url = "http://" + ip + ":" + port

# 검색엔진의 빌드 정보를 반환한다.
url = base_url

response = requests.get(url)
result = json.loads(response.text)
# print(json.dumps(result, indent=2, ensure_ascii=False))


# ### 3.1 형태소 분석
# ---
# 입력된 텍스트에 대한 형태소분석 결과를 반환한다.
# kana_url = "http://10.231.227.155:7578/ksm/kana/analyze"
# url = kana_url
#
# params = {
#     'mod':'kma',
#     'text':'입력된 텍스트에 대한 windows ㅋㅋ 형태소 분석 기반의 키워드 추출 결과를 반환한다.',
#     'format':'plain',
#     'charset':'utf8',
#     'language':'korean',
#     'option':'on'
# }

# response = requests.get(url, params=params)
# print(response.content.decode("utf8"))

# 15. /ksm/ner2 (개체명 분석)
# 15.1. /extract (개체명 추출)
# 인물, 지명, 기관, 전화번호 등의 개체명을 추출한다. GET, POST 방식을 지원한다
# kana_url = "http://10.231.227.155:7578/ksm/ner2"
# url = kana_url
#
# params = {
#     'text':'이효리는 입력된 텍스트에 대한 windows ㅋㅋ 형태소 분석 기반의 키워드 추출 결과를 반환한다.',
#     'format':'json',
#     'charset':'utf8',
#     'language':'korean'
#     # ,'option':''
# }
#
# response = requests.get(url, params=params)
# print(response.content.decode("utf8"))

# # 16. /ksm/plt (시각화) > output : javascript
# kana_url = "http://10.231.227.155:7578/ksm/plt"
# url = kana_url
#
# params = {
#     'type':'pie',
#     'format':'random',
#     # 'text':'이효리는 입력된 텍스트에 대한 windows ㅋㅋ 형태소 분석 기반의 키워드 추출 결과를 반환한다.',
#     'width':300,
#     'height':300,
#     'data':'a,60\n'+'b,30\n'+'d,40'
# }
#
# response = requests.get(url, params=params)
# print(response.content.decode("utf8"))
#


# 16. /ksm/plt (시각화) > output : javascript
kana_url = "http://10.231.227.155:7578/ksm/plt"
url = kana_url

params = {
    'type':'pie',
    'format':'random',
    # 'text':'이효리는 입력된 텍스트에 대한 windows ㅋㅋ 형태소 분석 기반의 키워드 추출 결과를 반환한다.',
    'width':300,
    'height':300,
    'data':'a,60\n'+'b,30\n'+'d,40'
}

response = requests.get(url, params=params)
print(response.content.decode("utf8"))