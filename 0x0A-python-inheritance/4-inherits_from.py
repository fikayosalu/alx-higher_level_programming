#!/usr/bin/python3
"""
4-inherits_from.py module
contains a function inherits_from
inherits_from accepts two arguments: obj and a_class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the obj is an instance of a class that inherited from
    a_class otherwise Return False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
