#!/usr/bin/env python3
"""Documented"""


def analyze(df):
    """Documented"""
    return df.describe(exclude=["Timestamp"])
