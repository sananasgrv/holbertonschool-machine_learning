#!/usr/env/bin python3
""""Documented module"""


def matrix_transpose(matrix):
    """Documented"""
    result = []
    for row in range(len(matrix[0])):
        result.append([matrix[col][row]  for col in range(len(matrix))])
    return result
