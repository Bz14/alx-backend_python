"""A module to implement make_multiplier """
from typing import Union, Tuple


def make_multiplier(multiplier: float) -> callable:
    """ A function that returns a function multiplier """
    def multiply(n: float) -> float:
        """ A function that multiplies a float """
        return n * multiplier
    return multiply


