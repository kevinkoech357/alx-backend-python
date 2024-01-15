#!/usr/bin/env python3

"""
Replace wait_n func with task_wait_random
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values)
    """
    delay: List[float] = []

    async def append_delay(delays: List[float]) -> None:
        delay = await task_wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(append_delay(delay) for _ in range(n)))

    return delay
