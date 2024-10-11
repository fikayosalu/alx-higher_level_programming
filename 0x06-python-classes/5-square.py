#!/usr/bin/python3
"""
5-square module
Contains a class Square
The Square class defines a square
"""


class Square:
    """
    Defines a square
    Contains 5 methods:
    The __init__ method
    An area method to calculate the area of the square
    A my_print method that prints the square with
    the character '#' to the stdout
    Getters and Setter methods
    """

    def __init__(self, size=0):
        """
        Initializes objects of the Square class
        with the size attribute, with an default size of 0
        The size attribute is a private attribute
        size must be an integer, otherwise raise TypeError
        exception with message "size must be an integer"
        If size < 0 raise ValueError exception with message
        "size must be >= 0 "
        """

        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must the >= 0")

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the size"""

        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must the >= 0")

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character '#'
        """
        if self.__size is 0:
            print()
        i = 0
        while i < self.__size:
            j = 0
            while j < self.__size:
                print("#", end="")
                j += 1
            print()
            i += 1
