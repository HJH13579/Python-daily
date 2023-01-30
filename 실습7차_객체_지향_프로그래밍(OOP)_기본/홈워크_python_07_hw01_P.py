class Doggy:
    
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

        Doggy.num_of_dogs += 1

    def bark(self):
        return 'bark!'

    def get_status(self):
        return self.birth_of_dogs, self.num_of_dogs

    def birth(self):
        self.num_of_dogs += 1
        self.birth_of_dogs += 1
        return self.birth_of_dogs, self.num_of_dogs
    
    def death(self):
        self.num_of_dogs -= 1
        return self.num_of_dogs

# dog_a = Doggy('해리', '푸들')
# dog_b = Doggy('론', '치와와')

# print(dog_b.get_status())

# dog_b.birth()

# print(dog_b.get_status())

# dog_b.death()

# print(dog_b.get_status())

# print(dog_b.bark())