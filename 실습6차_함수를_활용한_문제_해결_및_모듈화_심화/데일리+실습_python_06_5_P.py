# sum_of_digit(3904) # 16

num = int(input())

def sum_of_digit(num):

    if num == 0:
        return 0
    else:
        return sum_of_digit(num // 10) + (num % 10)


print(sum_of_digit(num))


# 더 수학적으로

num = int(input())

def sum_of_digit(num):

    quotient = num // 10
    remainder = num % 10

    if quotient == 0:
        return remainder
    else:
        return sum_of_digit(quotient) + remainder


print(sum_of_digit(num))

# 더더 수학적으로 

num = int(input())

def sum_of_digit(num):
    if num == 0:
        return 0
    
    quotient = num // 10
    remainder = num % 10
    
    return sum_of_digit(quotient) + remainder


print(sum_of_digit(num))

# Slicing으로 풀기

def func(number):
    
    print(number)
    number = str(number)

    if number == '':
        return 0
    return func(number[:-1]) + int(number[-1])

print(func(1234))

