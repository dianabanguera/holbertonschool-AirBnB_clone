#!/usr/bin/python3
"""Test base Model"""

import unittest
from models.base_model import BaseModel
from unittest import mock


class Test_Base_Model(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        """
        self.object = BaseModel()

    def test_init(self):
        """
        """
        self.assertIsInstance(self.object, BaseModel)

    def attr(self):
        """
        """
        object_string = str(self.object)
        obj_attr = ["id", "created_at", "updated_at"]
        counter = 0
        for attr in obj_attr:
            if attr in object_string:
                counter += 1
        self.assertEqual(counter, 3)

    def arg_class(self):
        """testing a class created with arguments"""
        class1 = BaseModel(__class__="test", id="123456789")
        self.assertEqual(type(class1), BaseModel)

    def kawargs(self):
        """testing kawargs"""
        class2 = BaseModel(name="pepito", age=18)
        test_dic = class2.to_dict()
        attributes = ["name", "age", "__class__"]
        attr_dic = list(test_dic.keys())
        self.assertCountEqual(attr_dic, attributes)

    @mock.patch("models.storage")
    def save(self, mock_engine):
        """testing the save method (updated dates)"""
        first_update = self.object.updated_at
        self.object.save()
        second_update = self.object.updated_at
        self.assertNotEqual(first_update, second_update)
        self.assertTrue(mock_engine.save.called)

    def to_dict(self):
        """testing the transform from object to dictionary"""
        self.object.name = "poncho"
        dict_object = self.object.to_dict()
        attributes = ["id", "name", "created_at", "updated_at", "__class__"]
        new_attr = list(dict_object.keys)
        self.assertCountEqual(new_attr, attributes)

    def value_dic(self):
        """testing the values of the dictionary"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.object.name = "poncho"
        dict_object = self.object.to_dict()
        self.assertEqual(dict_object["name"], "poncho")
        self.assertEqual(dict_object["created_at"],
                         self.object.created_at.strftime(time_format))
        self.assertEqual(dict_object["updated_at"],
                         self.object.created_at.strftime(time_format))
        self.assertEqual(dict_object["__class__"], "BaseModel")

    def test_str(self):
        """testing the string of the dictionary"""
        object_str = f"[BaseModel] ({self.object.id}) {self.object.__dict__}"
        self.assertEqual(object_str, str(self.object))


if __name__ == '__main__':
    unittest.main()