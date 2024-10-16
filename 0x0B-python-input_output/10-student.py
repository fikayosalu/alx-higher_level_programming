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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            dic = {}
            # Access the full dictionary of attributes
            attributes = self.__dict__
            for i in attrs:
                if i in attributes:
                    dic[i] = attributes[i]
            return dic

            # Print only 'name' and 'age'
            # return {key: attributes[key] for key in
            # attrs if key in attributes}

        return self.__dict__
