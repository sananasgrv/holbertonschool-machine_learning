#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf

def flip_image(image):
    """Documented"""
    flipped = tf.reverse(image, axis=[1])
    return flipped
