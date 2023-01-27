# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar

def year_leap():
    while 1:
        year = int(input())  

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print('윤년입니다. 연도를 다시 입력해주세요.')          
        else:
            print(calendar.calendar(year))
            
            year = int(input())
            month = int(input())
            day = int(input())

            week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

            if calendar.weekday(year, month, day) == 0:
                print('경고 월요일입니다.')
                dict_day = {'년': year, '월': month, '일': day, '요일': week[calendar.weekday(year, month, day)]}
                print(dict_day)
            
            else :
                dict_day = {'년': year, '월': month, '일': day, '요일': week[calendar.weekday(year, month, day)]}
                print(dict_day)
                
            break
            
    return

year_leap()

