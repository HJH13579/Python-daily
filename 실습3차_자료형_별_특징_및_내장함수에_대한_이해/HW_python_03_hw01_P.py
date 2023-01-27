year = int(input('윤년 판독기(연도) : '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('윤년')
else:
    print('윤년이 아니다')
