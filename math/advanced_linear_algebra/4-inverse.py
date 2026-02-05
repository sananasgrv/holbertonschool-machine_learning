#!/usr/bin/env python3
"""Documented"""
adjugate = __import__('3-adjugate').adjugate
determinant = __import__('0-determinant').determinant


def adjugate(matrix):
    """Documented"""
    adj_mat = adjugate(matrix)
    determinant_of_mat = determinant(matrix)
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = adj_mat[i][j] / determinant_of_mat
    return result
