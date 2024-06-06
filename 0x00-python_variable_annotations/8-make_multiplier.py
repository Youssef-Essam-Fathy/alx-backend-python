#!/usr/bin/env python3
"""
This module defines a function `make_multiplier` that returns a function
which multiplies its input by a specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the original multiplier.
    """
    def func(value: float) -> float:
        """
        Multiplies the input by the specified multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return func
