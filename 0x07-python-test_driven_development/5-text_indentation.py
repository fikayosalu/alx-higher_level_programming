#!/usr/bin/python3
"""
5-text_indentation.py
This module contains a function: text_indentation
The function prints a text with 2 lines after each of these
characters: '?', '.', ':'.
The function takes an argument
"""


def text_indentation(text):
    """
    Prints a text with2 new lines after each of these
    characters: '.', '?', ':'.
    'text' must be a string, otherwise raise a TypeError
    exception with the message: "text must be string"
    There should be no space at the beginning or at the end
    of each printed line.
    """

    if isinstance(text, str):
        i = 0
        array = list(text)
        while i < len(array):
            if array[i] == '.' or array[i] == '?' or array[i] == ':':
                array[i + 1] = '\n\n'
            i += 1
        string = "".join(array)
        print(string)
    else:
        raise TypeError("text must be a string")
