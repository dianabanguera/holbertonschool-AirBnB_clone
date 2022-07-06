"""This module contain the __init__ method"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
