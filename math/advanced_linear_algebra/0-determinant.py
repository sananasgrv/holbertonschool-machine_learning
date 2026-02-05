#!/usr/bin/env python3
"""Documented"""


def determinant(matrix):
    """Documented"""
    det = 0
    if matrix == [[]]:
        return 0
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a list of lists")
        if len(i) != len(matrix):
            raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for col in range(len(matrix)):
            sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det
