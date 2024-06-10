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

    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay) * max_delay
