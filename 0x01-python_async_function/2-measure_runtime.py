#!/usr/bin/env python3

"""Importing asyncio and time module"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of the wait_n coroutine.

    This function measures the total execution time
    for running the wait_n(n, max_delay)coroutine,
    which spawns 'n' coroutines each waiting for
    a random delay between 0 and 'max_delay' seconds.
    It then returns the average time taken for
    each of these coroutines to complete.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
        float: The average execution time per coroutine.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
