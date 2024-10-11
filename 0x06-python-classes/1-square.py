#!/bin/usr/python3
"""
1.square module
OOP Programming style
Contains a class Square
"""


class Square:
    """
    Has a private attribute "size"
    An object instance "size" white no type/value
    """

    def __init__(self, size):
        """
        constructor __init__ has gives the object instance
        attribute when created
        It contains the size attribute
        """

        self.__size = size
