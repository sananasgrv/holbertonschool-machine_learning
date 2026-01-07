#!/usr/bin/env python3
"""Documented"""
import pandas as pd

def from_numpy(array):
    """Documented"""
    df = pd.DataFrame(array, columns=[chr(i) for i in range(array.shape[1])])
    return df