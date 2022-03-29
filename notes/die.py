# die has number of sides, shape, value
# can roll(), get_value(), set_value()
# within a class you will always have a constructor and methods
from random import randint


class Die:
    def __init__(self, num_of_sides):
        self.sides = num_of_sides
        self.value = 1

    def get_value(self):
        return self.value

    def roll(self):
        new_value = randint(1, self.sides)
        self.value = new_value


def main():
    d = Die(6)
    d.roll()
    print(d.get.value())