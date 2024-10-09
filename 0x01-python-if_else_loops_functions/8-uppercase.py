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

    new_str = ""

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            new_str += chr(ord(i) - 32)
        else:
            new_str += i
    print("{}".format(new_str))
