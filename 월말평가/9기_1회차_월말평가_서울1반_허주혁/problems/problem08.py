# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    caesar_word = '' # 암호문 공백 할당, 채워넣기 위해

    for single_word in list(word): # for 구문을 위해 word를 list로 변환

        if single_word.isupper() == True: # 대문자일 경우
            
            cap_word = single_word
            num_cap = ord(cap_word) # 알파벳을 아스키 숫자로 변환 
            caesar_num_cap = num_cap + n # 시저 암호화

            if caesar_num_cap > 90: # 시저 암호화된 값이 알파벳 범위를 벗어난 경우
                caesar_num_cap = caesar_num_cap - 90 + 64 # 다시 처음으로 돌리기
            else:
                caesar_num_cap = caesar_num_cap

            caesar_word = caesar_word + chr(caesar_num_cap) # 시저 암호화 된 값을 알파벳으로 변환 후 넣기
        
        if single_word.isupper() == False: # 소문자일 경우

            uncap_word = single_word
            num_uncap = ord(uncap_word) # 알파벳을 아스키 숫자로 변환
            caesar_num_uncap = num_uncap + n    # 시저 암호화

            if caesar_num_uncap > 122: # 시저 암호화된 값이 알파벳 범위를 벗어난 경우 
                caesar_num_uncap = caesar_num_uncap - 97 + 71 # 다시 처음으로 돌리기 
            else: 
                caesar_num_uncap = caesar_num_uncap

            caesar_word = caesar_word + chr(caesar_num_uncap) # 시저 암호화 된 값을 알파벳으로 변환 후 넣기

    return caesar_word

    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
