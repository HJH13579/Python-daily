# collatz(6)  # => 8
# collatz(16)  # => 4
# collatz(27)  # => 111
# collatz(626331)  # => -1


class Collatz:

    def __init__(self, num):
        self.num = num

    def collatz(self):
        count = 0 

        while(1):
            if self.num != 1:
                if self.num % 2 == 0:
                    self.num = self.num / 2
                    count += 1
                elif self.num % 2 == 1:
                    self.num = 3 * self.num + 1
                    count += 1
            else:
                break
        
        if count <= 500:
            return count
        else:
            return -1 
        
n = int(input())

print(Collatz(n).collatz())