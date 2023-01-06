#!/usr/bin/python3
"""file for a type-annotated function make_multiplier
that takes a float multiplier as argument and
returns a function
that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float and returns a function that multiplier a float"""
    x: Callable[[float], float] = lambda f: multiplier * f
    return x
