#!/usr/bin/env python3
"""Documented"""


def matrix_shape(matrix):
    """Documented"""
    result = []
    result.append(len(matrix))
    if type(matrix[0]) is not list:
        return result
    else:
        return result + matrix_shape(matrix[0])
