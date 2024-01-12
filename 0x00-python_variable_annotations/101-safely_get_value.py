#!/usr/bin/env python3

"""
Define a function that safely gets a value from a dict
based on the key
"""


from typing import TypeVar, Any, Mapping, Union, Optional


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default:
        Optional[T] = None) -> Union[Any, T]:
    """
    Retrieve the value from the dictionary for the given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
