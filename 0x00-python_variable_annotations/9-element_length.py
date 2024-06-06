#!/usr/bin/env python3
"""Importing from typing module"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Given an iterable of sequences, returns a list of tuples where each tuple
    contains a sequence from the iterable and its corresponding length.

    Args:
    - lst (Iterable[Sequence]): An iterable containing sequences
    (e.g., lists, strings, tuples).

    Returns:
    - List[Tuple[Sequence, int]]: A list of tuples, each containing a
    sequence from the input iterable and its length.

    Example:
    >>> element_length(["hello", "world", "a", "test"])
    [('hello', 5), ('world', 5), ('a', 1), ('test', 4)]
    """
    return [(i, len(i)) for i in lst]
