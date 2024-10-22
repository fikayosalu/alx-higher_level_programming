#!/usr/bin/python3
"""
base module
Contains a class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write([])
            list_dict = [r.__dict__ for r in list_objs]
            file.write(Base.to_json_string(list_dict))
