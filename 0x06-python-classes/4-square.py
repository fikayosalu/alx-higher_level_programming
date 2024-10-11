#!/usr/bin/python3
"""
4-square module
Contains a class Square that defines a square
"""


class Square:
    """
    Defines a square
    It contains 4 methods
    The __init__ method to set the attributes of the square
    An area method to calculate the area of the square
    A setter and getter method
    """

    def __init__(self, size=0):
        """
        Initializes Objects of the Square class
        with the size attribute
        The size attribute is a private instance attribute
        """

        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
