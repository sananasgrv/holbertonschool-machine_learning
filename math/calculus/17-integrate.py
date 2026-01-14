#!/usr/bin/env python3
"""Documented"""


def poly_integral(poly, C=0):
    if type(poly) is not list or len(poly) == 0:
        return None
    elif type(C) is int:
        if poly == 0:
            return C
        else:
            result = [C]
            for i in range(len(poly)):
                result.append(poly[i] / (i+1))
                result[i] = int(result[i]) if result[i] % 1 == 0 else result[i]
        return result
    else:
        return None
