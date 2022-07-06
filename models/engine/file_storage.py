#!/usr/bin/python3
"""This module contain the class FileStorage"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from os import path


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __object = {}
    def all(self):
        """"""
        return self.__object
    def new(self, obj):
        """"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__object[key] = obj
    def save(self):
        """"""
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            data = {k: v.to_dict() for k, v in self.__object.items()}
            json.dump(data, file)
    def reload(self):
        """"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="UTF-8") as file:
                dic = json.loads(file.read())
                for k, v in dic.items():
                    self.__object[k] = eval(v["__class__"])(**v)
