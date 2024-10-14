#!/usr/bin/python3
"""
2-is_same_class module
It contains a function is_same_class
is_same_class takes two arguments: obj and a_class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
