lst_fruit = list(input().lower().split(','))

def fresh_fruits(lst):
    fresh_fruit = []
    for fruit in lst:
        if fruit[:6] == 'rotten':
            fresh_fruit.append(fruit[6:])
        else:
            fresh_fruit.append(fruit)

    return fresh_fruit

print(fresh_fruits(lst_fruit))