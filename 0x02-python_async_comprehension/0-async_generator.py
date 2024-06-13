#!/usr/bin/env python3
# 0-async_generator.py

"""Async Generator"""

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times awaiting 1 sec then yield a ran no btn 0-10"""
    for i in range(10):
        await sleep(1)
        yield 10 * random()
