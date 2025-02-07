#!/usr/bin/env python3
""" Basic async syntax """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for a random delay between 0 and max_delay """
    delays = [wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
