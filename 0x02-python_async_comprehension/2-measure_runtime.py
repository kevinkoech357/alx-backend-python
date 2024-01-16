#!/usr/bin/env python3

"""
Define a coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime measures the total runtime and returns it.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()

    return end_time - start_time
