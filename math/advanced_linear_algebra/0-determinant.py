#!/usr/bin/env python3
"""Documented"""


def determinant(matrix):
    """Documented"""
    det = 0
    if matrix == [[]]:
        return 0x0
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix[i]) != len(matrix):
            raise TypeError("matrix must be a list of lists")
    if len(matrix[0]) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(len(matrix)):
            minor =
