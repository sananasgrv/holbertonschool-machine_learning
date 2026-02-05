#!/usr/bin/env python3
"""Documented"""


def minor(matrix):
    """Documented"""
    minor_e = 0
    minor_mat = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a list of lists")
        if len(i) != len(matrix) or matrix == [[]]:
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return 1
    elif len(matrix) == 2:
        return matrix.reverse()
    else:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                minor_e =
                minor_mat.append(matrix[row][col])
