#!/usr/bin/env python3
"""
Async comprehension demonstration.
"""
import asyncio
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously generates a list of floats using async_generator.
    """
    return [i async for i in async_generator()]
