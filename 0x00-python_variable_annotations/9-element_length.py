#!/usr/bin/env python3

"""
Duck typing a provided function.
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains an element from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
