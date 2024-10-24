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
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 3)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        pass

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        obj_attr = [cls.to_dictionary(x) for x in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                file.write(cls.to_json_string(obj_attr))

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                attr_list = cls.from_json_string(content)
                instances = [cls.create(**x) for x in attr_list]
                return instances
        except FileNotFoundError:
            return []
