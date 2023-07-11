#!/usr/bin/env python3
''' An asynchronous coroutine that takes an integer argument, waits
and then returns it.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait for time in seconds and return the wait time. '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
