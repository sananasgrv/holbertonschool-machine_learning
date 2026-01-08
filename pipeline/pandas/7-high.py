#!/usr/bin/env python3
"""Documented"""


def high(df):
    """Documented"""
    df.sort_values(by=["High"], ascending=False)
    return df
