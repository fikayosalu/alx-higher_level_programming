#!/usr/bin/python3
"""
6-load_from_json_file module
Contains a function save_to_json_file
"""


import json


def load_from_json_file(filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
