#!/usr/bin/python3
"""
4-print_square.py
This module contains a function:
print_square
The print_square function has takes one argument
The function print a square with character '#'
"""


def print_square(size):
    """
    Prints a square with character '#'
    'size' is size length of the square
    'size' must be an iteger, otherwise raise a TypeError
    exception with the message: "size must be an integer"
    if 'size' is less than 0, raise a ValueError exception
    with the message: "size must be >= 0"
    if 'size' is a float and is less than 0, raise a
    TypeError exception with the message:
    "size must be an integer"
    """

    if isinstance(size, int):
        i = 0

        while i < size:
            j = 0
            while j < size:
                print('#', end="")
                j += 1
            print()
            i += 1
    else:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
