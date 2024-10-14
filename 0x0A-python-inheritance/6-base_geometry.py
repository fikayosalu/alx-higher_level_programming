#!/usr/bin/python3
"""
6-base_geometry module
contains a class BaseGeometry
"""


class BaseGeometry:
    """Contains a method that raises an exception"""
    def __init__(self):
        pass

    def area(self):
        """Prints an Exception message"""
        raise Exception("area() is not implemented")
