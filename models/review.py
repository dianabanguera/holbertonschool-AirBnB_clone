#!/usr/bin/python3
"""Review class - AirBnB clone"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Derfines the instances attributes of the class
    Public attributes:
    place_id: string
    user_id: string
    text: string
    """
    place_id = ""
    user_id = ""
    text = ""
