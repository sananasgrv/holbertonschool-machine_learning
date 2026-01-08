#!/usr/bin/env python3
"""Documented"""


def prune(df):
    """Documented"""
    new_df = df.dropna(subset=["Close"])
    return new_df
