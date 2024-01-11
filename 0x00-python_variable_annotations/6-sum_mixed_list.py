#!/usr/bin/env python3

"""
Define a function which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    Takes a list of mixed int and float
    and returns their sum
    """
    return sum(mxd_lst)
