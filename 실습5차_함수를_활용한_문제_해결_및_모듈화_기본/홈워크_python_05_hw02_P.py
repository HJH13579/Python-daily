# fn_d(91) 
# 출력 예시 
# 101

num = int(input())


def fn_d(n):
    
    d_num = sum(map(int,list(str(n)))) + n

    return d_num

def is_generator(n):

    generator = 0

    for i in range(len(list(str(n)))):
        generator = generator + ((10 ** i) + 1) * int(list(reversed(list(str(num))))[i])

    return generator


def is_selfnumber(n):




    return 



print(fn_d(num))

# print(list(reversed(list(str(num)))))