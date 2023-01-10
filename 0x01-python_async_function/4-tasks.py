#!/usr/bin/env python3
"""defines the task_wait_n function"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """"an async routine that n task_wait_random time"""
    iterables = [task_wait_random(max_delay) for i in range(n)]
    n_list = []
    count = 0
    for coro in asyncio.as_completed(iterables):
        earliest = await coro
        n_list.append(earliest)
    return n_list
