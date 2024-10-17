#!/usr/bin/python3
"""
10-square module
Contains a class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square
    Inherits from the class Rectangle
    """
    def __init__(self, size):
        """
        Initializes instance of Square with attributes
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the description of the Square class"""
        return f"[Square] {self.__size}/{self.__size}"
