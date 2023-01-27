orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

re_orders = orders.split(',')
one_orders = set(orders.split(','))

num_ice = 0

for x in re_orders:
    if '아이스' in x:
        num_ice += 1
    else:
        continue

print(f'아이스 음료 : {num_ice}잔\n')

for y in one_orders:
    print(f'{y} : {re_orders.count(y)}잔')