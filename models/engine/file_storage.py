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
import datetime
from os import path


class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self):
        """Public instance methods that returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """eturns the dictionary __objects sets
        in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Public instance methods serializes
        __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as file:
            data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Public instance methods deserializes the JSON file"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r",
                      encoding="UTF-8") as file:
                dic = json.loads(file.read())
                for k, v in dic.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)

    def class_dict(self):
        """Returns the class attribute '_-classes <dictionary>'
        wich strores the available Classes for all modules"""
        return FileStorage.__classes

    def attributes(self):
        """Method that contain all attributes"""
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
                }
        return attributes
