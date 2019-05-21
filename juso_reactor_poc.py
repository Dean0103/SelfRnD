# -*- coding: utf-8 -*-
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
import json
import requests

print('도로명주소 검색API 서비스를 이용한 주소검색결과를 보여줍니다.')
keystr = input('검색어를 입력하세요. : ')

resulttype= 'json'

url = 'http://www.juso.go.kr/addrlink/addrLinkApi.do'
queryParams = '?' + urlencode({ quote_plus('currentPage') : '1' , quote_plus('countPerPage') : '10',
                                quote_plus('resultType') : resulttype, quote_plus('keyword') : keystr, quote_plus('confmKey') : 'bGk3MHZtMWJ2anNkODIwMTQwOTEyMTg0NDI2' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

print("url = " + url)
print("keyword = " + keystr)
print("="*100)


if resulttype=='json':
    root_json = json.loads(response_body)
    print('<< results >>')
    print('totalCount   : ' + root_json['results']['common']['totalCount'])
    print('currentPage  : ' + root_json['results']['common']['currentPage'])
    print('countPerPage : ' + root_json['results']['common']['countPerPage'])
    print('errorCode    : ' + root_json['results']['common']['errorCode'])
    print('errorMessage : ' + root_json['results']['common']['errorMessage'])
    for child in root_json['results']['juso']:
        confmKey = 'U01TX0FVVEgyMDE5MDUxNzEwMDYzODEwODczNzQ= '
        admCd_n = child['admCd']    # 행정구역코드 : admCd
        rnMgtSn_n = child['rnMgtSn']  # 도로명코드 : rnMgtSn
        udrtYn_n = child['udrtYn']   # 지상 지하여부(0 : 지상, 1: 지하)
        buldMnnm_n = child['buldMnnm']
        buldSlno_n = child['buldSlno']
        bdMgtSn_n = child['bdMgtSn']


kana_url = "http://www.juso.go.kr/addrlink/addrCoordApiJsonp.do"
url = kana_url

params =        {
                   #quote_plus('url') : "http://www.juso.go.kr/addrlink/addrCoordApiJsonp.do",
                   quote_plus('confmKey') : "U01TX0FVVEgyMDE5MDUxNzEwMDYzODEwODczNzQ=" ,
                   quote_plus('admCd') : admCd_n,
                   quote_plus('rnMgtSn') : rnMgtSn_n,
                   quote_plus('udrtYn') : udrtYn_n,
                   quote_plus('buldMnnm') : buldMnnm_n,
                   quote_plus('buldSlno') : buldSlno_n,
                   quote_plus('bdMgtSn') : bdMgtSn_n
                   }

response = requests.get(url, params=params)

root_jsons = json.loads( response_body )

print( '<< results >>' )
for childs in root_jsons['results']['juso']:
    result_n = response.content.decode("utf8")
    print (result_n)


"""
for child in root_json['results']['juso']:
    confmKey = 'U01TX0FVVEgyMDE5MDUxNzEwMDYzODEwODczNzQ= '
    admCd_n = child['admCd']  # 행정구역코드 : admCd
    rnMgtSn_n = child['rnMgtSn']  # 도로명코드 : rnMgtSn
    udrtYn_n = child['udrtYn']  # 지상 지하여부(0 : 지상, 1: 지하)
    buldMnnm_n = child['buldMnnm']
    buldSlno_n = child['buldSlno']
    bdMgtSn_n = child['bdMgtSn']
"""


