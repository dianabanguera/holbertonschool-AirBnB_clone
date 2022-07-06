#!/usr/bin/python3
"""Unittest module for Amenity class that inherit of BaseModel"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestAmenity(unittest.TestCase):
    """This class do a test for Amenity class"""

    def config(self):
        """set up test"""
        pass

    def test_instance(self):
        """Test of instantiation of Amenity class"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertTrue(BaseModel, issubclass(type(obj)))
        self.assertEqual("<class 'models.amenity.Amenity'>", str(type(obj)))

    def test_attribute(self):
        """test that do test of attributes in Amenity class"""
        att = storage.attributes()["Amenity"]
        obj = Amenity()
        for key, value in att.items():
            self.assertEqual(hasattr(obj, key))
            self.assertTrue(type(getattr(obj, key, None)), value)

    def test_reset(self):
        """tets that reset FileStora data"""
        FileStorage._FileStorage__object = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
