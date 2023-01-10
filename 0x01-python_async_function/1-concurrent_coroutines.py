#!/usr/bin/env python3
"""defines the wait_n function"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """"an async routine that n wait_random time"""
    iterables = [wait_random(max_delay) for i in range(n)]
    n_list = []
    count = 0
    for coro in asyncio.as_completed(iterables):
        earliest = await coro
        n_list.append(earliest)
    return n_list
