# 1. 간단한 N의 약수

n = int(input())

for i in range(1, n+1):
    i = 1
    if n % i == 0:
        print(i, end = " ") # 가로로 출력

# 2. List의 합 구하기

lst = [1, 2, 3, 4, 5]

def list_sum(lst):
    result = 0
    for num in lst:
        result = result + num

    # print(result) 하지 않게 주의!
    return result

list_sum(lst)

# 3. Dictionary로 이루어진 List의 합 구하기

dic = [
    {'name': 'kim', 'age': 12},
    {'name': 'lee', 'age': 4}
]

def dict_list_sum(lst):
    result = 0
    for dic in lst:
        result += dic['age']
    return result

dict_list_sum(dic)

# 4. 2차원 List의 전체 합 구하기

lst = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

def all_list_sum(lst):
    result = 0
    for sub_list in lst:
        for num in sub_list:
            result += sum
    return result

all_list_sum(lst)

# 7. 강한 이름
# 아스키코드 = 딕셔너리, key = 숫자, value = 문자



def get_strong_word(word1, word2)
    print(word1, word2)

    result1 = 0 
    for char1 in word1:
        result1 += ord(char1) # 문자를 숫자로 변환
    
    result2 = 0 
    for char2 in word2:
        result2 += ord(char2)

    if result1 > result2:
        return word1
    elif result1 < result2:
        return word2
    else: 
        return word1, word2

get_strong_word('delilah', 'dixon')