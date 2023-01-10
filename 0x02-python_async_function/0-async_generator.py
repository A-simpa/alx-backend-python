#!/usr/bin/env python3
""""defines the async_generator"""
import asyncio
import random


async def async_generator():
    """yields a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
