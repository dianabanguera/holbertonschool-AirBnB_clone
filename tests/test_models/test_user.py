#!/usr/bin/python3
"""Test for User"""


from datetime import datetime
import os
import unittest

from attr import attributes
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """"Test class User"""

    def setUp(self):
        """Method setup"""
        pass

    def resetStorage(self):
        """Method reset"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Method tear"""
        self.resetStorage()
        pass

    def test_instance(self):
        """Testing instances"""
        new_user = User()
        self.assertEqual(str(type(new_user)), "<class 'models.user.User'>")
        self.assertIsInstance(new_user, User)
        self.assertTrue(issubclass(type(new_user), BaseModel))

    def test_attr(self):
        """Testing attributes"""
        attributes = {'email': str, 'password': str,
                      'first_name': str, 'last_name': str}
        new_user1 = User()
        for k, value in attributes.items():
            self.assertTrue(hasattr(new_user1, k))
            self.assertEqual(type(getattr(new_user1, k, None)), value)


if __name__ == "__main__":
    unittest.main()
