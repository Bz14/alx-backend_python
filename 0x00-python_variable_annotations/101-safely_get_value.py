#!/usr/bin/env python3
"""A module to implement safe_first_element """
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Function to safely get the value from a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
