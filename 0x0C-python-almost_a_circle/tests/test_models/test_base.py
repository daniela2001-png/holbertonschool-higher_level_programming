#!/usr/bin/python3

"""
Unittest for model or class base
"""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """
    testing model base
    """
    def test_my_id(self):
        """
        testeo cuanod mi id is None
        """
        my_id = Base()
        self.assertEqual(my_id.id, 1)

    def test_id(self):
        """
        testeo si id es != None
        """
        my_id = Base(89)
        self.assertEqual(my_id.id, 89)


if __name__ == '__main__':
    unittest.main()
