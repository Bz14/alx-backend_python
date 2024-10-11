#!/usr/bin/env python3
"""A module to implement element_length """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples of elements and their lengths """
    return [(i, len(i)) for i in lst]
