#!/usr/bin/env python3
"""Documented"""
import pandas as pd


df = pd.DataFrame({
    "First": pd.series([0.0, 0.5, 1.0, 1.5]),
    "Second": pd.Series(['one', 'two', 'three', 'four']),
}, index=list("AB"))
