#!/usr/bin/env python3
"""Documented"""
import numpy as np


def precision(confusion):
    """Documented"""
    TP = np.diagonal(confusion)
    FP = sum(confusion[: , len(confusion)])
