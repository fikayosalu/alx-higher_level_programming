#!/usr/bin/python3
"""
6-load_from_json_file module
Contains a function save_to_json_file
"""


from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def save_arg_in_json():
    """
    Writes an Object to a text file, using a JSON representation
    """
    filename = "add_item.json"

    try:
        args = load_from_json_file(filename)

    except FileNotFoundError:
        args = []
        save_to_json_file(args, filename)

    args.extend(argv[1:])
    save_to_json_file(args, filename)


save_arg_in_json()
