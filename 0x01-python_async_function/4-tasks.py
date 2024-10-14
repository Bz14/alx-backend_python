#!/usr/bin/env python3
""" Basic async syntax """
import asyncio
from typing import List
import time


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for a random delay between 0 and max_delay """
    delays = [task_wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
