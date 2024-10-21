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
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def update(self, *args, **kwargs):
        """Update the values of attributes"""
        self.id = kwargs.get('id') if 'id' in kwargs else self.id
        self.__width = kwargs.get('width') if 'width'\
            in kwargs else self.width
        self.__height = kwargs.get('height') if 'height'\
            in kwargs else self.height
        self.__x = kwargs.get('x') if 'x' in kwargs else self.__x
        self.__y = kwargs.get('y') if 'y' in kwargs else self.__y

        self.id = args[0] if len(args) > 0 else self.id
        self.__width = args[1] if len(args) > 1 else self.__width
        self.__height = args[2] if len(args) > 2 else self.__height
        self.__x = args[3] if len(args) > 3 else self.__x
        self.__y = args[4] if len(args) > 4 else self.__y

    def to_dictionary(self):
        dict_attr = {
                'x': self.__x, 'y': self.__y, 'id': self.id,
                'width': self.__width, 'height': self.__height
        }
        return dict_attr

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            j = 0
            for i in range(self.__x):
                print(" ", end="")
            while j < self.__width:
                print("#", end="")
                j += 1
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"
