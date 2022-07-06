#!/usr/bin/python3
"""Unittest module for Review class that inherit of BaseModel"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestReview(unittest.TestCase):
    """This class do a test for Review class"""

    def setUp(self):
        """set up test"""
        pass

    def tearDown(self):
        """reset storage and Tear down test"""
        self.resetStorage()
        pass

    def test_instance(self):
        """Test of instantiation of Review class"""
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertTrue(BaseModel, issubclass(type(obj)))
        self.assertEqual("<class 'models.review.Review'>", str(type(obj)))

    def test_attribute(self):
        """test that do test of attributes in Review class"""
        att = storage.attributes()["Review"]
        obj = Review()
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
