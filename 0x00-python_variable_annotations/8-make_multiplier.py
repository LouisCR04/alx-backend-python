#!/usr/bin/python3
# 8-make_multiplier.py

""" Type annotated fx """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Return function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier
