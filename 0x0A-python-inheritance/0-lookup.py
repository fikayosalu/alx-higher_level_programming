#!/usr/bin/python3
"""
0-lookup module
Contains a funtion lookup
that accepts an object as argument
"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object"""
    return dir(obj)
