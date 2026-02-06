#!/usr/bin/env python3
"""Documented"""


class Poisson:
    """Poisson class"""
    def __init__(self, data=None, lambtha=1.):
        self.data = data
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            self.lambtha = sum(data)/len(data)
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 2:
                raise ValueError("data must contain multiple values")
