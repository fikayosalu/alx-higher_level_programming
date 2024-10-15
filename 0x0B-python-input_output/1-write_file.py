#!/usr/bin/python3
"""
1-write_file.py module
Contains a function write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to text file and returns the number of characters
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
