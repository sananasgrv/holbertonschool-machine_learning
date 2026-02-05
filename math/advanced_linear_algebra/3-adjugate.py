#!/usr/bin/env python3
"""Documented"""
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Documented"""
    cofactor_matrix = cofactor(matrix)
    adjugate_matrix = []
    for row in zip(*cofactor_matrix):
        adjugate_matrix.append(list(row))
    return adjugate_matrix