#!/usr/bin/python3
"""
1-rectangle module
Contains a class Rectangle
The Rectangle class defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    Contains 5 methods:
    __init__ method with attributes: width, height
    Getter and setter methods for height and width
    """

    def __init__(self, width=0, height=0):
        """
        Initialize objects of the rectangle class with
        the width and height attributes
        The width and height attributes are private attributes
        width must be an integer, otherwise raise a TypeError
        exception with the message "width must be an integer"
        if width is less than 0, raise a ValueError exception
        with the message "width must be >= 0"
        The same exceptions go for height
        """

        if type(width) is int and width >= 0:
            self.__width = width
        elif type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is int and height >= 0:
            self.__height = height
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if type(value) is int and value >= 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if type(value) is int and value >= 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
