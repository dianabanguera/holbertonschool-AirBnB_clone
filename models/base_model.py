#!/usr/bin/python3
"""This module have the class BaseModel:"""
import uuid
from datetime import datetime
import models


format = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Constructor of class"""
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, format)
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Methods that print: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Methods that updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Methods that returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.__dict__["created_at"].isoformat()
        self.__dict__["updated_at"] = self.__dict__["updated_at"].isoformat()
        return self.__dict__
