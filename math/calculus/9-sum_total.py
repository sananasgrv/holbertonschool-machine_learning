#!/usr/bin/env python3
"""Documented"""


def summation_i_squared(n):
    """i from 1 to n """
    if type(n) is not int:
        return None
    else:
        number = list(range(1, n + 1))
        result = 0
        numbers = list(range(1, n + 1))
        result = 0
        result = map(lambda i: i ** 2, numbers)
        return sum(result)
