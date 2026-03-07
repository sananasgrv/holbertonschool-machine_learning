#!/usr/bin/env python3
"""Documented"""
import pickle
import os


def save(self, filename):
    """Obyekti pickle formatında fayla yadda saxlayır."""
    if not filename.endswith('.pkl'):
        filename += '.pkl'

    with open(filename, 'wb') as f:
        pickle.dump(self, f)

def load(filename):
    """Fayldan pickle formatlı DeepNeuralNetwork obyektini yükləyir."""
    if not os.path.exists(filename):
        return None

    with open(filename, 'rb') as f:
        return pickle.load(f)
