#!/usr/bin/python3
"""
5-rectangle module
Contains a class Rectangle
class Rectangle defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    It has multiple methods:
    __init__ method
    __str__ method
    Area method to calculate the area of a rectangle
    Perimeter method to calculate the perimeter of a rectangle
    Setter an Getter methods
    """

    def __init__(self, width=0, height=0):
        """
        Initialize objects of the Rectangle class with
        private attributes: width, height
        width and height must be integers
        width and height must be >= 0
        """

        if type(width) is int and width >= 0:
            self.__width = width
        elif type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is int and height >= 0:
            self.__height = height
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if type(value) is int and value >= 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) is int and value >= 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a display of the rectangle using '#'"""
        display = ""
        if self.__width == 0 or self.__height == 0:
            return display
        else:
            for i in range(self.__height):
                j = 0
                while j < self.__width:
                    display += '#'
                    j += 1
                if i < self.__height - 1:
                    display += '\n'
            return display

    def __repr__(self):
        """Return a string representation of the rectangle class"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when instance is deleted"""
        print("Bye rectangle...")
