#!/usr/bin/env python3
"""Documented"""


def prune(df):
    """Documented"""
    df["Close"].dropna()
    return df
