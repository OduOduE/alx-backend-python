#!/usr/bin/env python3
''' Takes list of int and floats, returns sum as floats. '''
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the list as a float"""
    return float(sum(mxd_lst))
