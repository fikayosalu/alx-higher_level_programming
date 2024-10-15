#!/usr/bin/python3
"""
0-read_file module
Contains a function read_file
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
