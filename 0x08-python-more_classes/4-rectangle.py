#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
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
        return self.__width
   
    @width.setter
    def width(self, value):
        if type(value) is int and value >= 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def heigth(self, value):
        if type(value) is int and value >= 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self__height)

    def __str__(self):
        display = ""
        if self.__width == 0 or self.__height == 0:
            return 0
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
        return f"Rectangle({self.__width}, {self.__height})"
