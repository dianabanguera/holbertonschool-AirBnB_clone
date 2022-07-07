#!/usr/bin/python3
"""Test for file storage"""


import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    """The test class"""
    def setUp(self):
        """Method setup"""
        self.storage = FileStorage()
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
        """Test instance"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(str(e.exception), msg)

    def test_attr(self):
        """Test attributte"""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def prueba_all_(self, line):
        """"""
        self.resetStorage()
        object = eval(line)()
        storage.new(object)
        key = f"{type(object).__name__}.{object.id}"
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], object)

    def test_all__base_model(self):
        """Tests all() method for BaseModel."""
        self.prueba_all_("BaseModel")

    def test_all__user(self):
        """Tests all() method for User."""
        self.prueba_all_("User")

    def test_all__state(self):
        """Tests all() method for State."""
        self.prueba_all_("State")

    def test_all__city(self):
        """Tests all() method for City."""
        self.prueba_all_("City")

    def test_all__amenity(self):
        """Tests all() method for Amenity."""
        self.prueba_all_("Amenity")

    def test_all__place(self):
        """Tests all() method for Place."""
        self.prueba_all_("Place")

    def test_all__review(self):
        """Tests all() method for Review."""
        self.prueba_all_("Review")

    def prueba_all(self, line):
        """Test for Method all"""
        self.resetStorage()
        dict_objects = [eval(line)() for i in range(1000)]
        [storage.new(obj) for obj in dict_objects]
        self.assertEqual(len(dict_objects), len(storage.all()))
        for s in dict_objects:
            key = f"{type(s).__name__}.{s.id}"
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], s)

    def test_alliple_base_model(self):
        """Tests all() method with many objects."""
        self.prueba_all("BaseModel")

    def test_alliple_user(self):
        """Tests all_multiple() method for User."""
        self.prueba_all("User")

    def test_alliple_state(self):
        """Tests all_multiple() method for State."""
        self.prueba_all("State")

    def test_alliple_city(self):
        """Tests all_multiple() method for City."""
        self.prueba_all("City")

    def test_alliple_amenity(self):
        """Tests all_multiple() method for Amenity."""
        self.prueba_all("Amenity")

    def test_alliple_place(self):
        """Tests all_multiple() method for Place."""
        self.prueba_all("Place")

    def test_alliple_review(self):
        """Tests all_multiple() method for Review."""
        self.prueba_all("Review")

    def test_all_no_args(self):
        """Tests all() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_all_excess_args(self):
        """Tests all() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def Prueba_new(self, line):
        """Test for Method new"""
        self.resetStorage()
        new = eval(line)()
        storage.new(new)
        key = f"{type(new).__name__}.{new.id}"
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], new)

    def test_new_base_model(self):
        """Tests new() method for BaseModel."""
        self.Prueba_new("BaseModel")

    def test_new_user(self):
        """Tests new() method for User."""
        self.Prueba_new("User")

    def test_new_state(self):
        """Tests new() method for State."""
        self.Prueba_new("State")

    def test_new_city(self):
        """Tests new() method for City."""
        self.Prueba_new("City")

    def test_new_amenity(self):
        """Tests new() method for Amenity."""
        self.Prueba_new("Amenity")

    def test_new_place(self):
        """Tests new() method for Place."""
        self.Prueba_new("Place")

    def test_new_review(self):
        """Tests new() method for Review."""
        self.Prueba_new("Review")

    def test_new_no_args(self):
        """Tests new() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        msg = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)

    def test_new_excess_args(self):
        """Tests new() with too many arguments."""
        self.resetStorage()
        b = BaseModel()
        with self.assertRaises(TypeError) as e:
            storage.new(b, 98)
        msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def prueba_save(self, line):
        """Test for Method save"""
        self.resetStorage()
        new_obj = eval(line)()
        storage.new(new_obj)
        key = f"{type(new_obj).__name__}.{new_obj.id}"
        storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        new_dict = {key: new_obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(new_dict)))
            f.seek(0)
            self.assertEqual(json.load(f), new_dict)

    def test_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.prueba_save("BaseModel")

    def test_save_user(self):
        """Tests save() method for User."""
        self.prueba_save("User")

    def test_save_state(self):
        """Tests save() method for State."""
        self.prueba_save("State")

    def test_save_city(self):
        """Tests save() method for City."""
        self.prueba_save("City")

    def test_save_amenity(self):
        """Tests save() method for Amenity."""
        self.prueba_save("Amenity")

    def test_save_place(self):
        """Tests save() method for Place."""
        self.prueba_save("Place")

    def test_save_review(self):
        """Tests save() method for Review."""
        self.prueba_save("Review")

    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def prueba_reload(self, line):
        """Test for Method Reload"""
        self.resetStorage()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        new_reload = eval(line)()
        storage.new(new_reload)
        key = f"{type(new_reload).__name__}.{new_reload.id}"
        storage.save()
        storage.reload()
        self.assertEqual(new_reload.to_dict(), storage.all()[key].to_dict())

    def test_reload_base_model(self):
        """Tests reload() method for BaseModel."""
        self.prueba_reload("BaseModel")

    def test_reload_user(self):
        """Tests reload() method for User."""
        self.prueba_reload("User")

    def test_reload_state(self):
        """Tests reload() method for State."""
        self.prueba_reload("State")

    def test_reload_city(self):
        """Tests reload() method for City."""
        self.prueba_reload("City")

    def test_reload_amenity(self):
        """Tests reload() method for Amenity."""
        self.prueba_reload("Amenity")

    def test_reload_place(self):
        """Tests reload() method for Place."""
        self.prueba_reload("Place")

    def test_reload_review(self):
        """Tests reload() method for Review."""
        self.prueba_reload("Review")

    def test_reload_no_args(self):
        """Tests reload() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_reload_excess_args(self):
        """Tests reload() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == "__main__":
    unittest.main()
