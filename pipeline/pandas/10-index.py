#!/usr/bin/env python3
"""Documented"""


def index(df):
    df = df.index(df["Timestamp"])
    return df