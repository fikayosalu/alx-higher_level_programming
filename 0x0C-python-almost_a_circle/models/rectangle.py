#!/usr/bin/python3
"""
rectangle module
Contains a class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Ininitialize instances of Rectangle with attributes"""
        super().__init__(id)
        self.__width = self.__validate_w_h("width", width)
        self.__height = self.__validate_w_h("height", height)
        self.__x = self.__validate_xy("x", x)
        self.__y = self.__validate_xy("y", y)

    @property
    def width(self):
        """Return the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""
        self.__width = self.__validate_w_h("width", value)

    @property
    def height(self):
        """Return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height"""
        self.__height = self.__validate_w_h("height", value)

    @property
    def x(self):
        """Return the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x"""
        self.__x = self.__validate_xy("x", value)

    @property
    def y(self):
        """Return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of y"""
        self.__y = self.__validate_xy("y", value)

    def __validate_w_h(self, name, value):
        """Validate all setter methods and instantiation of width and height"""
        if type(value) is not int:
            raise TypeError(f"{name} must be integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
        return value

    def __validate_xy(self, name, value):
        """Validate all setter methods and instantiation of x and y"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        return value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            j = 0
            while j < self.__width:
                print("#", end="")
                j += 1
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) - {self.__width}/{self.__height}"
