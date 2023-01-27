grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

grain_name = []

grain_cost = []

for tup in grain_lst:
    grain_name.append(tup[0])
    grain_cost.append(tup[1])

sorted_cost = sorted(grain_cost, reverse=True)

for tup in grain_lst:
    if sorted_cost[0] == tup[1]:
        print(tup[0])