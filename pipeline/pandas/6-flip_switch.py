#!/usr/bin/env python3
"""Documented"""


def flip_switch(df):
    """Documented"""
    df.sort_values(by=["Timestamp"], ascending=True, inplace=True)
    return df.T