#!/usr/bin/env python3
"""A module to implement make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """ A function that returns a function multiplier """
    def multiply(n: float) -> float:
        """ A function that multiplies a float """
        return n * multiplier

    return multiply
