#!/usr/bin/python3
"""Test for User"""


from datetime import datetime
import os
import unittest

from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """"Test class Place"""

    def setUp(self):
        """Method setup"""
        pass

    def Reset(self):
        """Method reset"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Method tear"""
        self.Reset()
        pass

    def test_instance(self):
        """Testing instances"""
        new_object = Place()
        self.assertEqual(str(type(new_object)), "<class 'models.place.Place'>")
        self.assertIsInstance(new_object, Place)
        self.assertTrue(issubclass(type(new_object), BaseModel))

    def test_attr(self):
        """Testing attributes"""
        attributes = {'city_id': str, 'user_id': str,
                      'name': str, 'description': str,
                      'number_rooms': int, 'number_bathrooms': int,
                      'max_guest': int, 'price_by_night': int,
                      'latitude': float, 'longitude': float,
                      'amenity_ids': list}
        new_obj1 = Place()
        for k, value in attributes.items():
            self.assertTrue(hasattr(new_obj1, k))
            self.assertEqual(type(getattr(new_obj1, k, None)), value)


if __name__ == "__main__":
    unittest.main()
