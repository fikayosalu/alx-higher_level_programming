#!/usr/bin/python3
"""
8-class_to_json module
Contains a function class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionarydescription with simple data structure
    for JSON serialization of an object
    """

    return obj.__dict__
