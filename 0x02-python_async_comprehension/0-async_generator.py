#!/usr/bin/env python3

"""
This module contains an asynchronous generator
that yields random floats between 0 and 10.
The generator is intended to demonstrate
the use of asynchronous programming in Python
to perform non-blocking operations.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields
    random floats between 0 and 10.

    This generator produces 10 random floats,
    each after a 1-second delay.
    It demonstrates the use of asynchronous
    generators to perform non-blocking
    operations while yielding values.

    Yields:
        float: A random float between 0 and 10 (inclusive).
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
