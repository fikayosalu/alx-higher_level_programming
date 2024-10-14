#!/usr/bin/python3
"""
3-is_kind_of_class module
contains a function is_kind_of_class
is_kind_of_class accepts two arguments: obj and a_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the obj is an instance of, or it the object
    instance of a class that inherited from a_class otherwise
    Return False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
