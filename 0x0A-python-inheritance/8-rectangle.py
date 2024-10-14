#!/usr/bin/python3
"""
8-base_geometry module
contains 2 classes BaseGeometry and Rectangle
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


class Rectangle(BaseGeometry):
    """Initializes the instance of Rectangle with width and height"""
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
