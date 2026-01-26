#!/usr/bin/env python3
"""Documented"""


def cat_arrays(arr1, arr2):
    """Documented"""
    result = arr1.copy()
    for i in arr2:
        result.append(i)
    return result
