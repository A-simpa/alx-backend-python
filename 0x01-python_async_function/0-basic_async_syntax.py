#!/usr/bin/env python3
"""defines an await function"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait-ranom waits for a random delay between 0 and max_delay"""
    n = random.uniform(0, max_delay + 1)
    asyncio.sleep(n)
    return (n)