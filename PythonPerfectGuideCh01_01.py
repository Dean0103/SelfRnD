##
# @package 파이썬 완변 가이드
# 파이썬 완변 가이드 도서 Study
# chap 01. Test
##

# 1장 Test
# @brief 1장 Test
# @author Dean
# @date 2019.03.13
# @version 1.0.0
# @details
# 1.
# 2.
# 3.
# 4.
# 변수명 | 설명
# ------- | -------
##

# 튜플 테스트
portfolio = [('GOOG', 100, 490.10), ('MSFT', 50, 54.23)]
# portfolio[0] = ('GOOG', 100, 490.10)
# portfolio[1] = ('MSFT', 50, 54.23)

total = 0.0
for name, shares, price in portfolio:
    total += shares * price

print(total)