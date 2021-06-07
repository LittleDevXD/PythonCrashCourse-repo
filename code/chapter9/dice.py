import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        print(random.randint(1, self.sides))

my_dice = Dice(110)
my_dice.roll_dice()