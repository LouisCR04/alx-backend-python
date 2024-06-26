#!/usr/bin/env python3
# 2-measure_runtime.py
"""Parallel comprehensions"""

from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Will execute async_comprehension 4 times in parallel using asyncio.gather
    Will then measure total runtime & return it
    """
    start = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    end = time()

    return end - start
