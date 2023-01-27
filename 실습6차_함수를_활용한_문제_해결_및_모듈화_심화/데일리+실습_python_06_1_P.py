# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(reg_num):
    
    if reg_num[6] == '-':
        new_num = reg_num[0:6] + '*' * len(reg_num[7:])
    else: 
        new_num = reg_num[0:6] + '*' * len(reg_num[6:])
        
    return new_num

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))
