#!/usr/bin/env python3
"""Documented"""


def fill(df):
    """Documented"""
    df = df.drop(columns=['Weighted_Price'])
    df["Close"] = df["Close"].ffill()
    df[["High", "Low", "Open"]] = (
        df[["High", "Low", "Open"]].fillna(df["Close"]).ffill())
    df[["Volume_(BTC)", "Volume_(Currency)"]] = (
        df[["Volume_(BTC)", "Volume_(Currency)"]].fillna(value=0))
    return df
