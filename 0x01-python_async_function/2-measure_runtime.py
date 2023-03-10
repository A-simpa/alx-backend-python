#!/usr/bin/env python3
"""defines the measure_time function"""
import asyncio
import time
import typing

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns the total time it takes wait_n"""
    s = time.perf_counter()
    asyncio.run(task_wait_random(n, max_delay))
    t = time.perf_counter()
    return ((t - s) / n)
