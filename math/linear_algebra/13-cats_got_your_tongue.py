#!/usr/bin/env python3
"""Documented"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Documented"""
    new_mat = np.concatenate((mat1, mat2), axis=axis)
    return new_mat
