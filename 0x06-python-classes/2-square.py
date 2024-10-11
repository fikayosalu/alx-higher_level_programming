#!/usr/bin/python3
"""
2-square module
contains a class Square
Square has a private attribute "size"
"""


class Square:
    """
    Defines a class Square
    Square has a private attribute
    """

    def __init__(self, size=0):
        """
        Initializes the Object instance with
        private attribute "size"
        Size must be an integer otherwise raise a TypeError
        exception with message "size must be an integer"
        If size is less than 0, raise a ValueError exception
        with the message "size must be >= 0"
        """

        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
