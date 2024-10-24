#!/usr/bin/pyhton3
"""
test_rectangle
Contains unit testing for the class Rectangle
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


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
        first = Rectangle(1, 2)
        self.assertEqual(first.id, 1)
        second = Rectangle(3, 4)
        self.assertEqual(second.id, 2)
        third = Rectangle(2, 3, 4)
        self.assertEqual(third.id, 3)
        int1 = Rectangle(4, 5, 2, 4, 1)
        self.assertEqual(int1.id, 1)
        int2 = Rectangle(3, 19, 4, 10, 12)
        self.assertEqual(int2.id, 12)
        int_4 = Rectangle(4, 5, 8, 3)
        self.assertEqual(int_4.id, 4)

    def test_validate_attr(self):
        """
        Test the validation of the values of the attributes
        of the class Rectangle
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "y", 2, 3)

        r1 = Rectangle(10, 3, 2, 1)
        self.assertEqual(r1.width, 10)

        with self.assertRaises(ValueError):
            r1.width = -2

        with self.assertRaises(ValueError):
            Rectangle(5, 7, -8, 3)

        r2 = Rectangle(4, 6, 6, 3, 7)
        self.assertEqual(r2.y, 3)

        with self.assertRaises(TypeError):
            r2.x = "7"

        with self.assertRaises(TypeError):
            Rectangle({}, {}, {}, {})

        with self.assertRaises(TypeError):
            Rectangle(10, [], 2, 3)

        r3 = Rectangle(10, 5, 3, 1)
        self.assertEqual(r3.x, 10)

        with assertRaise(ValueError):
            r3.y = -4

    def test_area(self):
        """ Test the area method of the Rectangle"""
        r1 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 6)
        self.assertEqual(r2.area(), 12)

        r3 = Rectangle(6, 5, 4, 5)
        self.assertEqual(r3.area(), 30)

        r4 = Rectangle(10, 9)
        self.assertEqual(r4.area(), 90)

        r5 = Rectangle(4, 6, 4, 5, 8)
        self.assertEqual(r5.area(), 24)

    def test_str(self):
        """Test the __str__ method of Rectangle"""
        r1 = Rectangle(1, 2, 5, 7)
        self.assertEqual(r1, [Rectangle] (1) 5/7 - 1/2)

        r2 = Rectangle(3, 4, 8, 9, 5)
        self.assertEqual(r2, [Rectangle] (5) 8/9 - 3/4)


if __name__ == "__main__":
    unittest.main()
