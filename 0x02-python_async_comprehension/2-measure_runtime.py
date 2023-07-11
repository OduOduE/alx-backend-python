#!/usr/bin/env python3
''' Execute async_comprehension parallelly x4 using asyncio.gather. '''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Return measured total runtime. '''
    start_runtime = time.time()
    await asyncio.gather(*(async_comprehension() for v in range(4)))
    end_runtime = time.time()

    return end_runtime - start_runtime
