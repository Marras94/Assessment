import random
class randomnumbers:
    def __init__(self):

        self.limit = int(input("How many numbers should be returned?: "))
        self.min = int(input("Enter the lowest number: "))
        self.max = int(input("Enter the highest number: "))
        self.retrive(self.limit, self.min, self.max)

    def retrive(self, limit, min, max):
        for i in range(limit):
            print(random.randint(min, max))

run = randomnumbers()