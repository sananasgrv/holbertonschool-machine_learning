#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf

def change_contrast(image, lower, upper):
    """Documented"""
    return tf.image.random_contrast(image,
                                    lower=lower, upper=upper)
