#!/usr/bin/env python3
# 0-basic_async_syntax.py

""" Basics of async """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for random delay btn 0 to max & returns it"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
