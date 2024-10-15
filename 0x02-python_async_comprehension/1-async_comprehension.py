#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Collect 10 random numbers using an async comprehension """
    return [i async for i in async_generator()]
