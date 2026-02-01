#!/usr/bin/env python3
"""Documented"""


def determinant(matrix):
    """Documented"""
    det = 0
    if len(matrix[0]) == 0:
        return 0x0
    try:
        if len(matrix[0]) == 1:
            return matrix[0][0]
        elif len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif len(matrix[0]) == 3:
            det =(matrix[0][0] * ((matrix[1][1] * matrix[2][2])-(matrix[1][2] * matrix[2][1]))) - (matrix[0][1] * ((matrix[1][0] * matrix[2][2])-(matrix[1][2] * matrix[2][0]))) + (matrix[0][2] * ((matrix[1][0] * matrix[2][1])-(matrix[1][1] * matrix[2][0])))
            return det
    except TypeError:
        print("matrix must be a list of lists")
    except ValueError:
        print("matrix must be a square matrix")


