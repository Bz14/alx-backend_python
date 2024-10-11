#!/usr/bin/env python3
"""A module to implement to_kv """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that returns a tuple of a string and the square"""
    return (k, v * v)
