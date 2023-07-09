#!/usr/bin/env python3
''' Takes a float, returns a function that multiplies the float. '''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    ''' Returns a function that multiplies a float by multiplier. '''
    def float_multi(x: float) -> float:
        return multiplier * x

    return float_multi
