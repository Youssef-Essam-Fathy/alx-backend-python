#!/usr/bin/env python3
"""No module importing"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function that takes a list input_list of floats as argument
    and returns their sum as a float
    """
    sum = 0.0
    for element in input_list:
        sum += element
    return sum
