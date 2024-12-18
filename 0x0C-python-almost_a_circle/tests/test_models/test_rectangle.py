#!/usr/bin/pyhton3
"""
test_rectangle
Contains unit testing for the class Rectangle
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
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
            r2.width = 5.6

        with self.assertRaises(TypeError):
            r2.width = True

        with self.assertRaises(TypeError):
            r2.width = False

        with self.assertRaises(TypeError):
            r2.width = []

        with self.assertRaises(TypeError):
            r2.width = {}

        with self.assertRaises(TypeError):
            r2.height = 5.6

        with self.assertRaises(TypeError):
            r2.height = True

        with self.assertRaises(TypeError):
            r2.height = False

        with self.assertRaises(TypeError):
            r2.height = {}

        with self.assertRaises(TypeError):
            r2.height = []

        with self.assertRaises(TypeError):
            Rectangle(5, 3.7)

        with self.assertRaises(TypeError):
            Rectangle(5, 37, 9.7)

        with self.assertRaises(TypeError):
            Rectangle(5, 3, 7, 4.5)

        with self.assertRaises(TypeError):
            Rectangle(True, 3)

        with self.assertRaises(TypeError):
            Rectangle(3, False)

        with self.assertRaises(TypeError):
            Rectangle(5, 3, True, 8)

        with self.assertRaises(TypeError):
            Rectangle(4, 7, 3, True)

        with self.assertRaises(TypeError):
            Rectangle({}, {}, {}, {})

        with self.assertRaises(TypeError):
            Rectangle(10, [], 2, 3)

        r3 = Rectangle(10, 5, 3, 1)
        self.assertEqual(r3.x, 3)

        with self.assertRaises(ValueError):
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
        self.assertEqual(str(r1), "[Rectangle] (1) 5/7 - 1/2")

        r2 = Rectangle(3, 4, 8, 9, 5)
        self.assertEqual(str(r2), "[Rectangle] (5) 8/9 - 3/4")

        r3 = Rectangle(3, 4)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 3/4")

        r4 = Rectangle(1, 3, 1)
        self.assertEqual(str(r4), "[Rectangle] (3) 1/0 - 1/3")

        r5 = Rectangle(4, 7, 8, 8, 0)
        self.assertEqual(str(r5), "[Rectangle] (0) 8/8 - 4/7")

    def test_update(self):
        """Test the update method used to assign values to attributes
        of the class
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.id, 1)

        r1.update(12)
        self.assertEqual(r1.id, 12)

        r1.update(width=12, height=16)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 16)

        r1.update(12, 34, 23, width=28, height=19, x=12)
        self.assertEqual(r1.width, 34)
        self.assertEqual(r1.height, 23)
        self.assertEqual(r1.x, 12)

        r1.update(3, 7, 8, 9, 2)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 2)

        r1.update(x=12, y=24, id=89)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 24)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 8)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        self.assertEqual(type(r1_dict), dict)
        self.assertEqual(r1_dict, {'x': 1, 'y': 9, 'id': 1,
                                    'height': 2, 'width': 10})
        r2 = Rectangle(12, 3, 7, 8, 2)
        r2_dict = r2.to_dictionary()
        self.assertEqual(type(r2_dict), dict)
        self.assertEqual(r2_dict, {
            'x': 7, 'y': 8, 'id': 2,
            'height': 3, 'width': 12
})
        r3 = Rectangle(2, 3)
        r3.update(**r2_dict)
        self.assertEqual(str(r3), "[Rectangle] (2) 7/8 - 12/3")

        r4 = Rectangle(2, 3)
        r4_dict = r4.to_dictionary()
        self.assertEqual(r4_dict, {
            'x': 0, 'y': 0, 'id': 3,
            'height': 3, 'width': 2
})

    def test_tojson_string(self):
        r2 = Rectangle(12, 3, 7, 8, 2)
        r2_dict = r2.to_dictionary()
        json_string = Base.to_json_string([r2_dict])
        self.assertEqual(json_string, json.dumps([{
            'x': 7, 'y': 8, 'id': 2,
            'width': 12, 'height': 3
}]))
        self.assertEqual(type(json_string), str)

        list_dict = [
        {'y': 8, 'x': 2, 'id': 1, 'width': 10, 'height': 7},
        {'y': 0, 'x': 0, 'id': 2, 'width': 2, 'height': 4}
]
        list_json = Base.to_json_string(list_dict)
        self.assertEqual(list_json, json.dumps([
            {'y': 8, 'x': 2, 'id': 1, 'width': 10, 'height': 7},
            {'y': 0, 'x': 0, 'id': 2, 'width': 2, 'height': 4}
]))
        self.assertEqual(type(list_json), str)

        dict_list = Base.to_json_string(None)
        self.assertEqual(dict_list, "[]")

        empty_list = Base.to_json_string([])
        self.assertEqual(empty_list, "[]")
        self.assertEqual(Base.to_json_string({'id': 12}),
                        json.dumps({'id': 12}))

    def test_save_to_file(self):
        r1 = Rectangle(1, 2, 3, 5)
        r2 = Rectangle(3, 5, 2, 7, 1)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, json.dumps([
                {'x': 3, 'y': 5, 'id': 1, 'width': 1, 'height': 2},
                {'x': 2, 'y': 7, 'id': 1, 'width': 3, 'height': 5}
            ]))

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")


if __name__ == "__main__":
    unittest.main()
