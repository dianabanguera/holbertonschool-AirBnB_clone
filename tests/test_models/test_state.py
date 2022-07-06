#!/usr/bin/python3
"""Unittest module for State class that inherit of BaseModel"""
import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestState(unittest.TestCase):
    """This class do a test for State class"""

    def setUp(self):
        """set up test"""
        pass

    def tearDown(self):
        """reset storage and Tear down test"""
        self.resetStorage()
        pass

    def test_instance(self):
        """Test of instantiation of State class"""
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertTrue(BaseModel, issubclass(type(obj)))
        self.assertEqual("<class 'models.State.State'>", str(type(obj)))

    def test_attribute(self):
        """test that do test of attributes in State class"""
        att = storage.attributes()["State"]
        obj = State()
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
