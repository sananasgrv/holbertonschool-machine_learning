#!/usr/bin/env python3
"""Documented"""


def analyze(df):
    """Documented"""
    df = df.drop(columns=['Timestamp'])
    return df.describe()
