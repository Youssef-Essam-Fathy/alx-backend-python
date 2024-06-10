#!/usr/bin/env python3

"""Importing asyncio and from typing modules"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create n tasks that wait for a random delay
    and return the sorted list of results.

    Args:
        n (int): number of tasks
        max_delay (int): maximum delay time

    Returns:
        List[float]: sorted list of random float results
    """
    my_list = [task_wait_random(max_delay) for _ in range(n)]

    result = await asyncio.gather(*my_list)

    sorted_result = sorted(result)

    return sorted_result
