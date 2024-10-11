#!/usr/bin/python3
"""
2-rectangle module
Contains a class Rectangle
class Rectangle defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    Contains multiple methods:
    __init__ method with two attributes: width, height
    getter and setter methods
    Area method to calculate the area of the rectangle
    Perimiter method to calculate the perimeter of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize objects of the rectangle class with
        width and height attributes
        width and height are private attributes
        width and height must be integers and >= 0
        """

        if type(width) is int and width >= 0:
            self.__width = width
        elif type(width) is not int:
            raise TypeError("width must be integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is int and height >= 0:
            self.__height = height
        elif type(height) is not int:
            raise TypeError("height must be integer")
        elif width < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is int and value >= 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is int and value >= 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
