#!/usr/bin/env python3

"""
Define a function that returns first el in a list.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
