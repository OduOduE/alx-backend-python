#!/usr/bin/env python3
''' Takes a string k, int OR float v and returns a tuple. '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Converts string, int or float to tuple. '''
    return (k, float(v**2))
