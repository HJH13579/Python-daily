# # # 입력 예시
# p1 = Point(1, 3)
# p2 = Point(3, 1)
# r1 = Rectangle(p1, p2)
# print(r1.get_area())
# print(r1.get_perimeter())
# print(r1.is_square())

# p3 = Point(3, 7)
# p4 = Point(6, 4)
# r2 = Rectangle(p3, p4)
# print(r2.get_area())
# print(r2.get_perimeter())
# print(r2.is_square())

# # 출력 예시
# # 4
# # 8
# # True

# # 9
# # 12
# # True

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Point와 Rectangle 간에 상속 관계가 없다고 볼 경우
# Rectangle를 만듬에 있어서 point가 필요하지 않다, 하지만 요소로서, point를 할용할 부품으로서 쓰인다.

class Rectangle(Point):
# class Rectangel: # 상속 관계가 없다고 보면

    # 가로, 세로 길이가 계속 쓰인다 = 변수로 만들자 

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    #   self.garo = abs(self.p1.x - self.p2.x) # 가로 세로 입력 안 받아도 된다, 왜냐하면 __init__은 초기화하는 함수지 입력 받는 함수가 아니니까
    #   self.sero = abs(self.p1.y - self.p2.y)
    
    # @property
    # def garo(self):
    #     return abs(self.p1.x - self.p2.x)

    def get_area(self): # 필요한 것은 가로 세로의 '길이'이지, p1, p2가 굳이 필요하지 않다. 굳이 p1, p2를 입력받지 않아도 된다.
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

        # garo = self.garo
        # sero = self.sero
        # return garo * sero


    def get_perimeter(self):
        return 2 * (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))

    def is_square(self):
        if self.p1.x == self.p2.x or self.p1.y == self.p2.y:
            return False
        else:
            return True

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())


