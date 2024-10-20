#!/usr/bin/python3
"""
base module
Contains a class Base
"""


class Base:
    """Manage the id attributes of all subclasses"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instance and subclasses of base with id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
