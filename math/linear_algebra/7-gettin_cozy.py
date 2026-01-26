#!/usr/bin/env python3
"""Documented"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Documented"""
    result = [row.copy() for row in mat1]

    if axis == 0:
        for i in range(len(mat2)):
            result.append(mat2[i])
    elif axis == 1:
        for j in range(len(mat1)):
            for_size = mat2[j]
            result[j].append(for_size[0])
    return result

