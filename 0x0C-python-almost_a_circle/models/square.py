#!/usr/bin/python3
"""
square module
Contains a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square and inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Rectangle class with attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Set the value of Square width and height"""
        self._Rectangle__width = \
            super()._Rectangle__validate_w_h("width", value)
        self._Rectangle__height = \
            super()._Rectangle__validate_w_h("width", value)

    def update(self, *args, **kwargs):
        """Update the values of attributes"""
        self.id = kwargs.get('id') if 'id' in kwargs else self.id
        self._Rectangle__width = kwargs.get('size') if 'size'\
            in kwargs else self._Rectangle__width
        self._Rectangle__height = kwargs.get('size') if 'size'\
            in kwargs else self._Rectangle__height
        self._Rectangle__x = kwargs.get('x') if 'x' \
            in kwargs else self._Rectangle__x
        self._Rectangle__y = kwargs.get('y') if 'y' \
            in kwargs else self._Rectangle__y

        self.id = args[0] if len(args) > 0 else self.id
        self._Rectangle__width = args[1] if len(args) > 1 \
            else self._Rectangle__width
        self._Rectangle__height = args[1] if len(args) > 1 \
            else self._Rectangle__height
        self._Rectangle__x = args[2] if len(args) > 2 else self._Rectangle__x
        self._Rectangle__y = args[3] if len(args) > 3 else self._Rectangle__y

    def to_dictionary(self):
        """Return a dictionary of the attributes and its values"""
        dict_attr = {
                'x': self._Rectangle__x, 'y': self._Rectangle__y,
                'id': self.id, 'size': self._Rectangle__width
        }
        return dict_attr

    def __str__(self):
        """Return the representation of the square class"""
        return f"[Square]  ({self.id}) {self._Rectangle__x}/\
{self._Rectangle__y} - {self._Rectangle__width}"
