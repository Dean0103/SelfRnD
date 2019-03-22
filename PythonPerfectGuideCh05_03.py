##
# @package 파이썬 완변 가이드
# 파이썬 완변 가이드 도서
# chap 5.
##

# 5장 Test
# @brief 5장 Test
# @author Dean
# @date 2019.03.20
# @version 1.0.0
# @details
# 1.
# 2.
# 3.
# 4.
# 변수명 | 설명
# ------- | -------
##

# 5.3.1 상관관계와 공분산
# pip3 install pandas_datareader --trusted-host pypi.org --trusted-host files.pythonhosted.org
import pandas as pd
from pandas_datareader import data

all_data = {}
for ticker in ['AAPL','IBM','MSFT','GOOG']:
    all_data[ticker] = data.DataReader(ticker, 'yahoo', '2015-01-01', '2016-01-01')

price = pd.DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})
volume = pd.DataFrame({tic: data['Volume'] for tic, data in all_data.items()})

returns = price.pct_change()
print(returns.tail())
print(returns.MSFT.corr(returns.IBM))
print(returns.MSFT.cov(returns.IBM))