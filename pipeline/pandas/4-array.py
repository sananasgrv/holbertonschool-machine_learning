#!/usr/bin/env python3
"""Documented"""


def array(df):
    """Documented"""
    new_df = df["High", "Close"].tail(10)
    return new_df.to_numpy()
