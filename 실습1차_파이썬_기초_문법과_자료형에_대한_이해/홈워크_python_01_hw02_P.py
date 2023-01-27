s = input('숫자를 입력해주세요 : ')

indivisual_s = map(int, (list(s))) # 자릿수를 개별 숫자로 쪼개기

print(sum(indivisual_s))