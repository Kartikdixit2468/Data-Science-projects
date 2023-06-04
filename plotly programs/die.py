from random import randint


class Die:
    """ Class to create a die """
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self):
        """Rolls the dice and retun the value"""
        return randint(1, self.sides)


if __name__ == '__main__':
    pass
