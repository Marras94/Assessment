import random

class randomnumbers:
    def __init__(self):
        print("Welcome!")
        print("Printing out random numbers for you: ")

        try:
            self.limit = int(input("How many numbers do you wan't? "))
            self.min = int(input("Enter the lowest number: "))
            self.max = int(input("Enter the highest number: "))

            self.retrive(self.limit, self.min, self.max)

        except:
            print("Error, please try again")

    def retrive(self, limit,min,max):
        for i in range(limit):
            print(random.randint(min, max))

run = randomnumbers()