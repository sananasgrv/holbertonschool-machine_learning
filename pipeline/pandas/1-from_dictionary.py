#!/usr/bin/env python3
"""Documented"""
import pandas as pd


df = pd.DataFrame(
    {
            "First": pd.Series([0.0, 0.5, 1.0, 1.5], dtype=float),
            "Second": pd.Series(["one", "two", "three", "four"], dtype=str),
        },
index=list("ABCD"))
