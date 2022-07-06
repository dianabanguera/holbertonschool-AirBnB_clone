#!/usr/bin/python3
"""Unittest module for City class that inherit of BaseModel"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestAmenity(unittest.TestCase):
    """This class do a test for City class"""

    def setUp(self):
        """set up test"""
        pass

    def tearDown(self):
        """reset storage and Tear down test"""
        self.resetStorage()
        pass

    def test_instance(self):
        """Test of instantiation of City class"""
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertTrue(BaseModel, issubclass(type(obj)))
        self.assertEqual("<class 'models.amenity.City'>", str(type(obj)))

    def test_attribute(self):
        """test that do test of attributes in City class"""
        att = storage.attributes()["City"]
        obj = City()
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
