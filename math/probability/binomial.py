#!/usr/bin/env python3
"""Documented"""


class Binomial:
    """Binomial"""
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n < 0:
                raise ValueError("n must be a positive value")
            if 0<=p and p<=1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = float(sum(data))/len(data)
            variance = float((sum(
                [(data[i] - mean) ** 2 for i in range(len(data))]
            ) / len(data)) ** 0.5)
            self.p = 1-((variance**2)/mean)
            self.n = int(round(mean / self.p))
            self.p = float(mean / self.n)
