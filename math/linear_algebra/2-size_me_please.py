#!/usr/bin/env python3
"""Documented"""


def matrix_shape(matrix):
    """Documented"""
    result = []
    result.append(len(matrix))
    result.append(len(matrix[0]))
    try:
        for_size = matrix[0]
        result.append(len(for_size[0]))
        print(result)
    except TypeError:
        print(result)

