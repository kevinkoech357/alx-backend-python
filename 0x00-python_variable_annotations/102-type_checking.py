#!/usr/bin/env python3

"""
Validating with mypy.
"""

from typing import Tuple, Any, List


from typing import List, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms in the input tuple by repeating each element by the specified factor.
    """
    zoomed_in: List[Any] = [item for item in lst for _ in range(factor)]
    return tuple(zoomed_in)


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: Tuple[Any, ...] = zoom_array(array)

zoom_3x: Tuple[Any, ...] = zoom_array(array, 3)
