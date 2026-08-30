#! /usr/bin/env python3
"""Comment of File"""
import gymnasium as gym

def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """Comment of Function"""
    env = gymk.make("FrozenLake-v1",
                    desc = desc,
                    map_name = map_name
                    is_slippery = is_slippery)
    return env
