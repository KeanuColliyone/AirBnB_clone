#!/usr/bin/python3
"""This module defines a class FileStorage for serializing and
deserializing instances."""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime

class FileStorage:
    """A class that serializes instances to a JSON file and
    deserializes JSON file to instances."""
    
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def reload(self):
        """Reloads the stored objects from __file_path."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                try:
                    obj_dict = json.load(f)
                    for obj_id, obj_attrs in obj_dict.items():
                        cls_name = obj_attrs["__class__"]
                        cls = self.classes().get(cls_name)
                        if cls:
                            self.__objects[obj_id] = cls(**obj_attrs)
                except Exception as e:
                    print(e)

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        return {
            "BaseModel": {"id": str, "created_at": datetime.datetime, "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {
                "city_id": str, "user_id": str, "name": str, "description": str, 
                "number_rooms": int, "number_bathrooms": int, "max_guest": int, 
                "price_by_night": int, "latitude": float, "longitude": float, 
                "amenity_ids": list
            },
            "Review": {"place_id": str, "user_id": str, "text": str}
        }
