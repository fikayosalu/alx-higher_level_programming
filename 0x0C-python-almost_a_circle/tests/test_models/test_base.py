#!/usr/bin/python3

import unittest
from models.base import Base

class TestBaseId(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_none(self):
        first = Base()
        self.assertEqual(first.id, 1)
        second = Base()
        self.assertEqual(second.id, 2)
        third = Base()
        self.assertEqual(third.id, 3)

    def test_integer(self):
        int1 = Base(1)
        self.assertEqual(int1.id, 1)
        int2 = Base(12)
        self.assertEqual(int2.id, 12)
        int3 = Base(90)
        self.assertEqual(int3.id, 90)

    def test_mix(self):
        int_1 = Base(32)
        self.assertEqual(int_1.id, 32)
        int_2 = Base()
        self.assertEqual(int_2.id, 1)
        int_3 = Base(72)
        self.assertEqual(int_3.id, 72)
        int_4 = Base()
        self.assertEqual(int_4.id, 2)


if __name__ == "__main__":
    unittest.main()
