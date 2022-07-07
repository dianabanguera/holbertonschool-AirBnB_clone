#!/usr/bin/python3
"""
This module is used to test the BaseModel class
"""


import unittest
from models.base_model import BaseModel
from unittest import mock


class TestBaseModel(unittest.TestCase):
    """
    Test for the class 'BaseModel'
    """

    def setUp(self):
        """set up test"""
        self.Object = BaseModel()

    def testInit(self):
        """reset storage and Tear down test"""
        self.assertIsInstance(self.Object, BaseModel)

    def testAttr(self):
        """Test number of attributes"""
        obj_str = str(self.Object)
        obj_attr = ["id", "created_at", "updated_at"]
        num = 0
        for attr in obj_attr:
            if attr in obj_str:
                num += 1
        self.assertEqual(num, 3)

    def argClass(self):
        """Test argumento give to class"""
        class_1 = BaseModel(__class__='test', id='555666777')
        self.assertEqual(type(class_1), BaseModel)

    @mock.patch("models.storage")
    def testSave(self, mock_engine):
        """Test update to update_at"""
        first_update = self.Object.updated_at
        self.Object.save()
        second_update = self.Object.updated_at
        self.assertNotEqual(first_update, second_update)
        self.assertTrue(mock_engine.save.called)

    def test_to_dict(self):
        """Test print with to_dict method"""
        self.Object.name = "Tulio"
        dic_obj = self.Object.to_dict()
        attributes = ["id", "name", "created_at", "updated_at", "__class__"]
        real_attr = list(dic_obj.keys())
        self.assertCountEqual(real_attr, attributes)

    def test_values_dict(self):
        """Test values in dict"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.Object.name = "Tulio"
        dic_obj = self.Object.to_dict()
        self.assertEqual(dic_obj["name"], "Tulio")
        self.assertEqual(dic_obj["created_at"],
                         self.Object.created_at.strftime(time_format))
        self.assertEqual(dic_obj["updated_at"],
                         self.Object.updated_at.strftime(time_format))
        self.assertEqual(dic_obj["__class__"], "BaseModel")

    def test_str(self):
        """Test information in __str__ method"""
        obj_str = f"[BaseModel] ({self.Object.id}) {self.Object.__dict__}"
        self.assertEqual(obj_str, str(self.Object))


if __name__ == "__main__":
    unittest.main()
