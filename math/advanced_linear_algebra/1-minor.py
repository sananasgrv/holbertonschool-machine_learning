#!/usr/bin/env python3
"""Documented"""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Documented"""
    minor_e = 0
    minor_mat = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a list of lists")
        if len(i) != len(matrix) or matrix == [[]]:
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sub_matrix = [row[:j] + row[j+1:] for
                              row in (matrix[:i] + matrix[i+1:])]
                minor_mat[i][j] = determinant(sub_matrix)
        return minor_mat
