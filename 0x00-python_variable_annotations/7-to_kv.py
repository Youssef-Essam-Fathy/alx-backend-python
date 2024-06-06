#!/usr/bin/env python3
"""Importing Union from typing module"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that returns a tuple

    Args:
        k (str): a string
        v (int | float): a string

    Returns:
        tuple[str, float]: a tuple
    """
    return (k, v * v)
