import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return random.randint(1, self.sides)


dice6 = Dice()

for i in range(10):
    print(dice6.roll_dice())

dice10 = Dice(10)

print()

for i in range(20):
    print(dice10.roll_dice())

print()

dice20 = Dice(20)

for i in range(10):
    print(dice20.roll_dice())




