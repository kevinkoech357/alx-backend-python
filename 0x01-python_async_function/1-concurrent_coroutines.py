#!/usr/bin/env python3


"""
Define an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values)
    """
    delay: List[float] = []

    async def append_delay(delays: List[float]) -> None:
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(append_delay(delay) for _ in range(n)))

    return delay
