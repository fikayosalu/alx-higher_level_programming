#!/usr/bin/python3
"""
7-base_geometry module
contains a class BaseGeometry
"""


class BaseGeometry:
    """Contains a multiple methods"""
    def __init__(self):
        pass

    def area(self):
        """Prints an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        return value
