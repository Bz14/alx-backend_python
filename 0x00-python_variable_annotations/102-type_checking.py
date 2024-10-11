#!/usr/bin/env python3
"""A module to implement mypy validate"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Use a tuple instead of a list

zoom_2x = zoom_array(array)  # This works fine
zoom_3x = zoom_array(array, 3)  # Pass an integer for the factor
