#!/usr/bin/python3
"""
9-student module
Contains a class Student
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes instance of class Student with public attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
