#!/usr/bin/python3
"""
7-islower.py module
It contains the function "islower"
The function takes in one argument and checks
if its true
"""


def islower(c):
    """
    Returns true if 'c' is lowercase
    otherwise it returns false
    """

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
