str_lst = input('문자열을 입력하세요. : ').lower().split()
num_words = len(str_lst)

n = 0

for i in range(num_words - 1):
    if str_lst[i][len(str_lst[i]) - 1] == str_lst[i + 1][0]:
        n += 1
    else:
        continue

if n == num_words -1:
    print('Pass')
else:
    print('Fail')