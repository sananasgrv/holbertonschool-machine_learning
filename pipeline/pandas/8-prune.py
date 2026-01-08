#!/usr/bin/env python3
"""Documented"""


def prune(df):
    """Documented"""
    df.dropna(subset=["Close"])
    return df
