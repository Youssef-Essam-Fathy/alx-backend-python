#!/usr/bin/env python3

"""Importing asyncio and random modules"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    """wait for printing a random value

    Args:
        max_delay (int, optional): max delay. Defaults to 10.

    Returns:
        _type_: _description_
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
