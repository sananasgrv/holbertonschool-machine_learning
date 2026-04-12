#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf


def change_hue(image, delta):
    """Documented"""
    return tf.image.adjust_hue(image, delta=delta)