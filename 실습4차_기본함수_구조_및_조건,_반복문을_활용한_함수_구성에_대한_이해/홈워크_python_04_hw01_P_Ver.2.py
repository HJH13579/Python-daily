words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
flag = False # 더미 데이터 : 기본값이 False


for idx in range(1, len(words)):
    print(idx)
    
    # 지금의 나

    if words[idx-1][-1] != words[idx][0]:
        print('실패', idx, words[idx])
        flag = True

    else:
    #    성공했을 때 => 겹침
        for sub_idx in range(idx): 
            pre_word = words[sub_idx]
            me_word = words[idx]
            if pre_word == me_word:           # True 일 때 Break를 원한다면
                print('실패', idx, words[idx])
                flag = True
                break    
    
    if flag:
        break


