#!/usr/bin/env python3
"""Documented"""


def fill(df):
    """Documented"""
    df = df.drop(columns=['Weighted_Price'])
    df["Close"] = df["Close"].ffill()
    df = df.fillna(subset=["High", "Low", "Open"], value=df["Close"])
    df = df.fillna(subset=["Volume_(BTC)","Volume_(Currency)"], value=0)
    return df