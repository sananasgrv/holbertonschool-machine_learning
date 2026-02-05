#!/usr/bin/env python3
"""Documented"""
adjugate = __import__('3-adjugate').adjugate
determinant = __import__('0-determinant').determinant


def inverse(matrix):
    """Documented"""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)

    if matrix == [] or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    adj_mat = adjugate(matrix)
    determinant_of_mat = determinant(matrix)
    if determinant_of_mat == 0:
        return None
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = adj_mat[i][j] / determinant_of_mat
    return result
