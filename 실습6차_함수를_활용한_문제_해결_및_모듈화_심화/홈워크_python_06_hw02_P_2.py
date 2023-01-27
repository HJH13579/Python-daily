# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

str = input()
result = str
for char in str:
    if char in "[]'":
        result = result.replace(char, "")

lst = result.split(",")

def group_anagrams(str):
    for i in len(lst):
        z

# def group_anagrams(str):
#     anagrams_list = []
#     for word1 in lst:
#         for word2 in lst:
#             if sorted(list(word1)) == sorted(list(word2)):
#                 anagrams_list.append(word1)
#                 anagrams_list.append(word2)
#     return anagrams_list

print(lst)
print(group_anagrams(str))



