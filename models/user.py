#!/usr/bin/python3
"""User class - AirBnB clone"""

from models.base_model import BaseModel


class User(BaseModel):
    """Derfines the instances attributes of the class
    Public attributes:
    email: String
    password: String
    first_name: String
    last_name: String
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
