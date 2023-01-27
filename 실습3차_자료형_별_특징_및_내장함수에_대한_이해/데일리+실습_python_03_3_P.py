# infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

infos = input()

age = 0

for dct in infos:
    age = age + dct['age']

print(age)