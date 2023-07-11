#!/usr/bin/env python3
''' This code is nearly identical to wait_n. '''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Spawn wait_random n times. '''
    '''wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
        )
    return sorted(wait_times)
    '''
    tasks = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
