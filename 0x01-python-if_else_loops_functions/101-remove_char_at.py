#!/usr/bin/python3
"""
101-remove_char_at module
It contains 1 function: "remove_char_at"
"remove_char_n" has two arguments
"""


def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character
    at position 'n'
    'str' is string
    'n' is an integer that represents the position the
    character to b removed
    """

    new_str = ""

    for i in range(len(str)):
        if i == n:
            continue
        else:
            new_str += str[i]
    return new_str
