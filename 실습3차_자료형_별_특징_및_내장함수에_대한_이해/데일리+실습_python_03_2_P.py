lst_words = input().split(',')

def middle_word(lst):
    if len(lst) % 2 == 0:
        print(lst[(len(lst) // 2) - 1], lst[len(lst) // 2])
    else:
        print(lst[len(lst) // 2])

    return 

middle_word(lst_words)