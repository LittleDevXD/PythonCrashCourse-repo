from random import randint

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Return random numbers between 1 and num_sides both inclusive"""
        return randint(1, self.num_sides)