#!/usr/bin/env python3
"""Documented"""


def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    result = []
    for i in range(len(mat1[0])):
        result.append([mat1[j][i] + mat2[j][i]for j in range(len(mat1))])
    return result
