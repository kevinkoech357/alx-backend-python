#!/usr/bin/env python3

"""
Returns asyncio.Task
"""


import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Returns asyncio.Task
    """
    loop = asyncio.get_event_loop()

    return loop.create_task(wait_random(max_delay))
