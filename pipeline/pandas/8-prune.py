#!/usr/bin/env python3
"""Documented"""


def prune(df):
    """Documented"""
    df["Close"].dropna(how="any")
    return df
