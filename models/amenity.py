#!/usr/bin/python3
"""This module creates an Amenity class that inherits from BaseModel."""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class for managing amenity objects within the HBNB project.
    
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
