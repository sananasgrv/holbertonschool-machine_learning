#!/usr/bin/env python3
"""Documented"""


def add_arrays(arr1, arr2):
    """Documented"""
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[j] for j in range(len(arr2)))
    return result
