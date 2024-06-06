#!/usr/bin/env python3
"""No module importing"""
def sum_list(input_list: 'list[float]') -> float:
    """
    function that takes a list input_list of floats as argument
    and returns their sum as a float
    """
    # [e1, e2, e3,...] -> sum = e1 + e2 + e3
    sum = 0
    for element in input_list:
        sum += element
    return sum
    