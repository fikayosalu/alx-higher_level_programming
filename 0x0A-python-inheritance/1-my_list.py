#!/usr/bin/python3
"""
contains a class Mylist
Mylist inherits from list
"""


class MyList(list):
    """Contains a method that sorts lists"""

    def print_sorted(self):
        """Prints a list but sorted (ascending order)"""
        print(sorted(self))
