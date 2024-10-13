#!/usr/bin/python3
"""
0-add_integer.py

This module provides a function to add 2 integers

Function:
- add_integer(a, b=98): Returns the sum of a and b
"""


def add_integer(a, b=98):
    """Returns the sum of a and b

    a and b must be intergers or float, otherwise\
    raise a TypeError exception with the message\
    "a must be an integer" or "b must be an integer"

    a or b must be casted to integers if they are floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
