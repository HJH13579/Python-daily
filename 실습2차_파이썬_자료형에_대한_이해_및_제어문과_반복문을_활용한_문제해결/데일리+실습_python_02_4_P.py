# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

price = 50000
VAT = 0.15
price_total = price + int(price * VAT)

print('스테이크' + '   ' + format(price, ',d'))
print('+ VAT' + '     ' + format(int(price*VAT), ',d'))
print('총계 ₩' + '    ' + format(int(price_total), ',d'))
