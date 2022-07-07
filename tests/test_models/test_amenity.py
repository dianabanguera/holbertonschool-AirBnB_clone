#!/usr/bin/python3
"""Test for Amenity inherits for Base Model"""

from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
import os


class TestAmenity(unittest.TestCase):
    """Class test amenity"""

    def setUp(self):
        """Method setup"""
        pass

    def resetStorage(self):
        """method reset storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """method teardown"""
        self.resetStorage()
        pass

    def test_instance(self):
        """test instance"""
        new_object = Amenity()
        self.assertEqual(str(type(new_object)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(new_object, Amenity)
        self.assertTrue(issubclass(type(new_object), BaseModel))

    def test_attr(self):
        """test attributes"""
        attributes = {'name': str}
        new_obj = Amenity()
        for k, value in attributes.items():
            self.assertTrue(hasattr(new_obj, k))
            self.assertEqual(type(getattr(new_obj, k, None)), value)


if __name__ == "__main__":
    unittest.main()
