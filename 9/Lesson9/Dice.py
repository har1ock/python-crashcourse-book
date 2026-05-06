from random import randint


class Dice:
    """"Кидок грального кубика"""

    def __init__(self, sides=6 ):
        self.sides = sides

    def roll_dice(self,):
        """Кинути кубик"""
        number = randint(1, self.sides)
        print(f'You rolled {number}')


dice1 = Dice()
dice2 = Dice(10)
dice3 = Dice(20)

for x in range(10):
    dice1.roll_dice()
    dice2.roll_dice()
    dice3.roll_dice()
