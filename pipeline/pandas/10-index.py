#!/usr/bin/env python3
"""Documented"""


def index(df):
    df = df.set_index("Timestamp")
    return df
