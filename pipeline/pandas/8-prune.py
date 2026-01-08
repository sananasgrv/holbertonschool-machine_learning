#!/usr/bin/env python3
"""Documented"""


def prune(df):
    """Documented"""
    df["Low"].dropna(how="any")
    return df