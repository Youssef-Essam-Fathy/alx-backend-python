#!/usr/bin/env python3

"""Importing asyncio, random and from typing modules"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait for n times to print a random list of floats

    Args:
        n (int): number of times
        max_delay (int): maximum delay time

    Returns:
        List[float]: list of random float result
    """
    my_list = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    result = await asyncio.gather(*my_list)

    sorted_result = sorted(result)

    return sorted_result
