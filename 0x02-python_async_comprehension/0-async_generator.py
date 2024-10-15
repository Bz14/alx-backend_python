#!/usr/bin/env python3
""" Async Generator module """
import asyncio
import random


async def async_generator() -> float:
    """ Coroutine that loops 10 times, yields a random number """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
