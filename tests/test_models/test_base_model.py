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
        """
        """
        self.Object = BaseModel()

    def testInit(self):
        """
        """
        self.assertIsInstance(self.Object, BaseModel)

    def testAttr(self):
        """
        """
        obj_str = str(self.Object)
        obj_attr = ["id", "created_at", "updated_at"]
        num = 0
        for attr in obj_attr:
            if attr in obj_str:
                num += 1
        self.assertEqual(num, 3)

    def argClass(self):
        """
        """
        class_1 = BaseModel(__class__='test', id='555666777')
        self.assertEqual(type(class_1), BaseModel)

    def testKwargs(self):
        """
        """
        class_2 = BaseModel(name="prueba", age=15)
        test_dict = class_2.to_dict()
        attributes = ["name", "age", "__class__"]
        attr_dict = list(test_dict.keys())
        self.assertCountEqual(attr_dict, attributes)

    @mock.patch("models.storage")
    def testSave(self, mock_engine):
        """
        """
        first_update = self.Object.updated_at
        self.Object.save()
        second_update = self.Object.updated_at
        self.assertNotEqual(first_update, second_update)
        self.assertTrue(mock_engine.save.called)

    def test_to_dict(self):
        """
        """
        self.Object.name = "Tulio"
        dic_obj = self.Object.to_dict()
        attributes = ["id", "name", "crated_at", "updated_ at", "__class__"]
        real_attr = list(dic_obj.keys())
        self.assertCountEqual(real_attr, attributes)

    def test_values_dict(self):
        """
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.Object.name = "Tulio"
        dic_obj = self.Object.to_dict()
        self.assertEqual(dic_obj["name"], "Tulio")
        self.assertEqual(dic_obj["crated_at"],
                         self.Object.created_at.strftime(time_format))
        self.assertEqual(dic_obj["updated_at"],
                         self.Object.updated_at.strftime(time_format))
        self.assertEqual(dic_obj["__class__"], "BaseModel")

    def test_str(self):
        """
        """
        obj_str = f"[BaseModel] ({self.Object.id}) {self.Object.__dict__}"
        self.assertEqual(obj_str, str(self.Object))


if __name__ == "__main__":
    unittest.main()
