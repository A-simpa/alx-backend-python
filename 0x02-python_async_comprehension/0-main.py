#!/usr/bin/env python3
"""defines async generator function"""
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    """creates an async generator"""
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
