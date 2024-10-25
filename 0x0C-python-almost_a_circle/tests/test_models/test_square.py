#!/usr/bin/pyhton3
"""
test_rectangle
Contains unit testing for the class Rectangle
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


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
        int2 = Square(3, 19, 4, 12)
        self.assertEqual(int2.id, 12)
        int_4 = Square(4, 5, 8)
        self.assertEqual(int_4.id, 4)

    def test_validate_attr(self):
        """
        Test the validation of the values of the attributes
        of the class Square
        """
        with self.assertRaises(TypeError):
            Square(10, "y", 2, 3)

        r1 = Square(10, 3, 2, 1)
        self.assertEqual(r1.size, 10)

        with self.assertRaises(ValueError):
            r1.size = -2

        with self.assertRaises(ValueError):
            Square(5, 7, -8, 3)

        r2 = Square(4, 6, 3, 7)
        self.assertEqual(r2.y, 3)

        with self.assertRaises(TypeError):
            r2.x = "7"

        with self.assertRaises(TypeError):
            r2.x = 5.6

        with self.assertRaises(TypeError):
            r2.x = True

        with self.assertRaises(TypeError):
            r2.x = False

        with self.assertRaises(TypeError):
            r2.y = 5.6

        with self.assertRaises(TypeError):
            r2.y = False

        with self.assertRaises(TypeError):
            r2.y = True

        with self.assertRaises(TypeError):
            r2.x = {}

        with self.assertRaises(TypeError):
            r2.x = []

        with self.assertRaises(TypeError):
            r2.y = {}

        with self.assertRaises(TypeError):
            r2.y = []

        with self.assertRaises(TypeError):
            r2.size = 5.6

        with self.assertRaises(TypeError):
            r2.size = True

        with self.assertRaises(TypeError):
            r2.size = False

        with self.assertRaises(TypeError):
            r2.size = []

        with self.assertRaises(TypeError):
            r2.size = {}

        with self.assertRaises(TypeError):
            r2.size = 5.6

        with self.assertRaises(TypeError):
            r2.size = True

        with self.assertRaises(TypeError):
            r2.size = False

        with self.assertRaises(TypeError):
            r2.size = {}

        with self.assertRaises(TypeError):
            r2.size = []

        with self.assertRaises(TypeError):
            Square(5, 3.7)

        with self.assertRaises(TypeError):
            Square(5, 37, 9.7)

        with self.assertRaises(TypeError):
            Square(5, True, 7)

        with self.assertRaises(TypeError):
            Square(True, 3)

        with self.assertRaises(TypeError):
            Square(3, False)

        with self.assertRaises(TypeError):
            Square(5, 3, True, 8)

        with self.assertRaises(TypeError):
            Square(4, 7, False)

        with self.assertRaises(TypeError):
            Square({}, {}, {}, {})

        with self.assertRaises(TypeError):
            Square(10, [], 2, 3)

        r3 = Square(10, 5, 3, 1)
        self.assertEqual(r3.x, 5)

        with self.assertRaises(ValueError):
            r3.y = -4

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

    def test_str(self):
        """Test the __str__ method of Rectangle"""
        r1 = Square(1, 2, 5)
        self.assertEqual(str(r1), "[Square] (1) 2/5 - 1")

        r2 = Square(3, 8, 9, 5)
        self.assertEqual(str(r2), "[Square] (5) 8/9 - 3")

        r3 = Square(3, 4)
        self.assertEqual(str(r3), "[Square] (2) 4/0 - 3")

        r4 = Square(1, 3, 1)
        self.assertEqual(str(r4), "[Square] (3) 3/1 - 1")

        r5 = Square(4, 8, 8, 0)
        self.assertEqual(str(r5), "[Square] (0) 8/8 - 4")

        r5 = Square(4)
        self.assertEqual(str(r5), "[Square] (4) 0/0 - 4")

    def test_update(self):
        """Test the update method used to assign values to attributes
        of the class
        """
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(r1.id, 10)

        r1.update(12)
        self.assertEqual(r1.id, 12)

        r1.update(size=12, x=16)
        self.assertEqual(r1.size, 12)
        self.assertEqual(r1.x, 16)

        r1.update(12, 34, 23, size=28, y=19, x=12)
        self.assertEqual(r1.size, 34)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.x, 23)

        r1.update(3, 7, 8, 9)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.size, 7)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 9)

        r1.update(x=12, y=24, id=89)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 24)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 7)

    def test_to_dictionary(self):
        r1 = Square(10, 1, 9)
        r1_dict = r1.to_dictionary()
        self.assertEqual(type(r1_dict), dict)
        self.assertEqual(r1_dict, {'x': 1, 'y': 9, 'id': 1,
                 'size': 10})
        r2 = Square(12, 7, 8, 2)
        r2_dict = r2.to_dictionary()
        self.assertEqual(type(r2_dict), dict)
        self.assertEqual(r2_dict, {
            'x': 7, 'y': 8, 'id': 2,
            'size': 12
})
        r3 = Square(2)
        r3.update(**r2_dict)
        self.assertEqual(str(r3), "[Square] (2) 7/8 - 12")

        r4 = Square(2)
        r4_dict = r4.to_dictionary()
        self.assertEqual(r4_dict, {
            'x': 0, 'y': 0, 'id': 3,
            'size': 2
})

    def test_tojson_string(self):
        r2 = Square(12, 7, 8, 2)
        r2_dict = r2.to_dictionary()
        json_string = Base.to_json_string([r2_dict])
        self.assertEqual(json_string, json.dumps([{
            'x': 7, 'y': 8, 'id': 2,
            'size': 12,
}]))
        self.assertEqual(type(json_string), str)

        list_dict = [
        {'y': 8, 'x': 2, 'id': 1, 'size': 10},
        {'y': 0, 'x': 0, 'id': 2, 'size': 2}
]
        list_json = Base.to_json_string(list_dict)
        self.assertEqual(list_json, json.dumps([
            {'y': 8, 'x': 2, 'id': 1, 'size': 10},
            {'y': 0, 'x': 0, 'id': 2, 'size': 2}
]))
        self.assertEqual(type(list_json), str)
        dict_list = Base.to_json_string(None)
        self.assertEqual(dict_list, "[]")

        empty_list = Base.to_json_string([])
        self.assertEqual(empty_list, "[]")
        self.assertEqual(Base.to_json_string({'id': 12}),
                        json.dumps({'id': 12}))



if __name__ == "__main__":
    unittest.main()
