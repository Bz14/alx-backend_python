#!/usr/bin/env python3
"""A module to implement safe_first_element """
from typing import Union, Any, Sequence, List


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function that returns the first element of a list or None"""
    if lst:
        return lst[0]
    else:
        return None
