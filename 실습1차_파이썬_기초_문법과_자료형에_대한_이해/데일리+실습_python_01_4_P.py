sum_x = 0

for x in range(1000):
    if (x % 2 == 0) or (x % 7 == 0):
        sum_x = sum_x + x

print(sum_x)