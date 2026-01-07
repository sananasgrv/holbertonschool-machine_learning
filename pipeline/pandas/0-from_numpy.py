#!/usr/bin/env python3
"""Documented"""
import pandas as pd

def from_numpy(array):
    """Documented"""
    df = pd.DataFrame(array)
    df.sort_values(by="A", ascending=True)
    return df