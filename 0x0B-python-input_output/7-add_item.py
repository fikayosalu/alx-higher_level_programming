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
    args = []
    save_to_json_file(args, "add_item.json")
    save_to_json_file(history, "add_item.json")
    i = 1
    print(history)
    if len(argv) > 1:
        while i < len(argv):
            if argv[i] not in history:
                history.append(argv[i])
            i += 1
    print(history)
    save_to_json_file(history, "add_item.json")


save_arg_in_json()
