#!/usr/bin/python3
"""
3-say_my_name.py

contains the function: say_my_name
The function takes two arguments:
first_name, last_name
The funtion prints to stdout:
"My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """Prints to stdout:
    "My name is <first name> <last name>"
    "first name" and "last name" must be strings
    otherwise raise a TypeError exception with the message:
    "first_name must be a string" or "Last_name must be a string"
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print(f"My name is {first_name} {last_name}")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
