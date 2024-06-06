#!/usr/bin/env python3
"""Importing List from typing module"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_summary_
        function which takes a list mxd_lst of integers and floats
        and returns their sum as a float
    Args:
        mxd_lst (List[Union[int, float]]): _description_

    Returns:
        float: _description_
    """
    sum = 0
    for element in mxd_lst:
        sum += element
    return sum
