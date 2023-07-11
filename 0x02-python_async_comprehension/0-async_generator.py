#!/usr/bin/env python3
''' Async..ly loop 10times, yeilding random number < 10 '''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Randomly generates 10 numbers less than 10 '''
    for i in range(10):
        await asyncio.sleep(1)  # Asynchronous operation
        yield random.random() * 10
