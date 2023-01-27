s_triangle = list(map(int, input().split()))
new_s_triangle = sorted(s_triangle)

if new_s_triangle[0] == new_s_triangle[1] == new_s_triangle[2]:
    print('정삼각형')

elif (new_s_triangle[0] == new_s_triangle [1]) or (new_s_triangle[1] == new_s_triangle[2]):
    print('이등변삼각형')

elif (new_s_triangle[0] ** 2) + (new_s_triangle[1] ** 2) == (new_s_triangle[2] ** 2):
    print('직각삼각형')

elif (new_s_triangle[0] + new_s_triangle[1]) > new_s_triangle[2]:
    print('삼각형')

else:
    print('삼각형 아님')