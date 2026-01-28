#!/usr/bin/env python3
"""Documented"""


def mat_mul(mat1, mat2):
    """Documented"""
    result = []
    for i in range(len(mat1)):
        result.append([0 for j in range(len(mat2[0]))])
    if len(mat1[0]) != len(mat2):
        return None
    else:
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                result[i][j] = mat1[i][j] * mat2[j][i]
        return result
