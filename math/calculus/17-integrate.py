#!/usr/bin/env python3
"""Documented"""


def poly_integral(poly, C=0):
    if type(poly) is not list or len(poly) == 0:
        return None
    if type(C) is not int:
        return None

    result = [C]

    for i in range(len(poly)):
        val = poly[i] / (i + 1)
        if val.is_integer():
            val = int(val)
        result.append(val)

    return result
