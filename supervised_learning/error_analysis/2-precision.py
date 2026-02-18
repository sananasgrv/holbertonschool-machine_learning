#!/usr/bin/env python3
"""Documented"""
import numpy as np


def precision(confusion):
    """Documented"""
    TP = np.diagonal(confusion)
    for i in range(len(confusion)):
        FP = sum(confusion[: , i])
    return TP/(TP+FP)
