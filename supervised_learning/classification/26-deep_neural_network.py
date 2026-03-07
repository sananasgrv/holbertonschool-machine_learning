#!/usr/bin/env python3
"""Documented"""
import pickle
import os


def save(self, filename):
    """saves the instance object to a file"""
    if not filename.endswith(".pkl"):
        filename += ".pkl"

    with open(filename, "wb") as f:
        pickle.dump(self, f)


@staticmethod
def load(filename):
    """loads a pickled object"""
    if not os.path.exists(filename):
        return None

    with open(filename, "rb") as f:
        return pickle.load(f)