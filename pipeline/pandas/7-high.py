#!/usr/bin/env python3
"""Documented"""


def high(df):
    """Documented"""
    df.sort_values(by=["High"], ascending=True)
    return df