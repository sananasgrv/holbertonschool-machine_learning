#!/usr/bin/env python3
""""Documented"""
import numpy as np


class Neuron:
    """Neuron"""
    def __init__(self, nx, b=0, A=0):
        if not type(nx) == int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.W = np.random.randn(1, nx)
        self.b = b
        self.A = A
