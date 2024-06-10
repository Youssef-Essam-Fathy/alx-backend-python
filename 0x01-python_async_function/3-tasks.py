#!/usr/bin/env python3
"""Importing asyncio module"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task
    for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds
        for the wait_random coroutine.

    Returns:
        asyncio.Task: A task object that schedules
        the wait_random coroutine.
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
