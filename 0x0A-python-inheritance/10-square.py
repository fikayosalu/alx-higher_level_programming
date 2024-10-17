#!/usr/bin/python3
"""
10-square module
contains 3 classes BaseGeometry,Rectangle, square
"""


class BaseGeometry:
    """Contains a multiple methods"""
    def __init__(self):
        pass

    def area(self):
        """Prints an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        return value


class Rectangle(BaseGeometry):
    """Initializes the instance of Rectangle with width and height"""
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a description of the Rectangle class"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    def __init__(self, size):
        """Initialize instance of the class with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


