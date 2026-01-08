#!/usr/bin/env python3
"""Documented"""


def fill(df):
    """Documented"""
    df = df.drop(columns=["Weighted_Price"])
    df = df.fillna(subset=["Close"], )
    return df