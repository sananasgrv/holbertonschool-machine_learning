#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf


def change_brightness(image, max_delta):
    """Documented"""
    return tf.image.random_brightness(image, max_delta=max_delta)