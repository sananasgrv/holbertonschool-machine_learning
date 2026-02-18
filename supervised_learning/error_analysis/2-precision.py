#!/usr/bin/env python3
"""Documented"""
import numpy as np


def precision(confusion):
    """Documented"""
    TP = np.diagonal(confusion)
    P = np.sum(confusion, axis=0)
    return TP/P
