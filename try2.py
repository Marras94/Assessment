import random
class randomnumbers:
    def __init__(self):
        try:
            self.limit = int(input("How many numbers should be returned?: "))
            self.min = int(input("Enter the lowest number: "))
            self.max = int(input("Enter the highest number: "))
            self.retrive(self.limit, self.min, self.max)

        except:
            print("Error, please try again!")
    def retrive(self, limit, min, max):
        for i in range(limit):
            print(random.randint(min, max))

run = randomnumbers()