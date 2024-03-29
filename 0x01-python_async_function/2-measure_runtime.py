#!/usr/bin/env python3

"""
Define a function that measures the total execution time
for wait_n(n, max_delay), and returns total_time / n
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time using
    time module.
    """
    s = time.time()

    asyncio.run(wait_n(n, max_delay))

    total_time = time.time() - s

    return total_time / n
