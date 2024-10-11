#!/usr/bin/python3
"""
3-square module
Contains a Square class
The Square class defines a square
"""


class Square:
    """
    Defines a square
    Contains 2 methods:
    The constructor __init__ method
    An area method
    """

    def __init__(self, size=0):
        """
        Initializes the Square class with a size attribute
        size must be an integer, otherwise raise TypeError
        exception with the message "size must be an integer"
        If size is less than 0, raise a ValueError exception
        with the message "size must be >= 0"
        """

        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
