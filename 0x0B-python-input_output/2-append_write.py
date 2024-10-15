#!/usr/bin/python3
"""
2-append_write module
Contains a function append_file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and
    returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
