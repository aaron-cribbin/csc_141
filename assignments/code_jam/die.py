# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

from random import randint


class Die:
    """A class representing a single d6."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)