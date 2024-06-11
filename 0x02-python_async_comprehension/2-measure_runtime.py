#!/usr/bin/env python3

"""
This module contains an asynchronous function to measure the runtime of
running four async comprehensions in parallel.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    """
    Measures the total runtime of executing async_comprehension
    four times  in parallel.

    Returns:
        float: The total runtime in seconds.
    """

    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
