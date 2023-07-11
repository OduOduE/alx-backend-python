#!/usr/bin/env python3
''' Uses async comprehensing over async_generator. '''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Uses async comprehensing over async_generator. '''
    random_numbers = [value async for value in async_generator()]
    return random_numbers
