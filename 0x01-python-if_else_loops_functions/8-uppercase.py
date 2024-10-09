#!/usr/bin/python3
"""
8-uppercase module
Contains 1 function: "uppercase"
"Uppercase" prints a string in Uppercase
Its has one argument
"""


def uppercase(str):
    """
    prints a string in uppercase
    """

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print(i, end="")
    print()
