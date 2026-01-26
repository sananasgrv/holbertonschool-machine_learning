#!/usr/bin/env python3
"""Documented"""


def add_arrays(arr1, arr2):
    """Documented"""
    result = []
    if len(arr1) != len(arr2):
        return None
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result
