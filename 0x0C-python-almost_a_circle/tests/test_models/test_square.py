#!/usr/bin/pyhton3
"""
test_rectangle
Contains unit testing for the class Rectangle
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """
    Every method of the class Rectangle is being tested
    """

    def setUp(self):
        """Set at thye beginning of every test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """
        To test the id attribute inherited from the Base class
        """
        first = Square(1, 2)
        self.assertEqual(first.id, 1)
        second = Square(3, 4)
        self.assertEqual(second.id, 2)
        third = Square(2, 3, 4)
        self.assertEqual(third.id, 3)
        int1 = Square(4, 5, 2, 1)
        self.assertEqual(int1.id, 1)
        int2 = Square(3, 19, 4, 10)
        self.assertEqual(int2.id, 10)
        int_4 = Square(4, 5, 8, 3)
        self.assertEqual(int_4.id, 3)

    def test_validate_attr(self):
        """
        Test the validation of the values of the attributes
        of the class Rectangle
        """
        with self.assertRaises(TypeError):
            Square(10, "y", 2, 3)

        r1 = Square(10, 3, 2, 1)
        self.assertEqual(r1.width, 10)

        with self.assertRaises(ValueError):
            r1.size = -2

        with self.assertRaises(ValueError):
            Square(5, 7, -8, 3)

        r2 = Square(4, 6, 6, 3)
        self.assertEqual(r2.y, 6)

        with self.assertRaises(TypeError):
            r2.x = "7"

        with self.assertRaises(TypeError):
            Square({}, {}, {}, {})

        with self.assertRaises(TypeError):
            Square(10, [], 2, 3)

        with self.assertRaises(TypeError):
            Square(10, True, 5, 4)

        r3 = Square(4, 6, 6, 3)
        self.assertEqual(r3.id, 3)

        with self.assertRaises(TypeError):
            r3.size = False

    def test_area(self):
        """ Test the area method of the Rectangle"""
        r1 = Square(2, 3, 4, 5)
        self.assertEqual(r1.area(), 4)

        r2 = Square(2)
        self.assertEqual(r2.area(), 4)

        r3 = Square(6, 5, 4, 5)
        self.assertEqual(r3.area(), 36)

        r4 = Square(10, 9)
        self.assertEqual(r4.area(), 100)

        r5 = Square(4, 6, 4, 5)
        self.assertEqual(r5.area(), 16)


if __name__ == "__main__":
    unittest.main()
