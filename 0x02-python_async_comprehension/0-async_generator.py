#!/usr/bin/env python3

"""
Define a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield a random value between 0 - 10
    and sleep for a sec in between.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
