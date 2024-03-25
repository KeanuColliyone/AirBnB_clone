#!/usr/bin/python3
"""This module creates a City class that inherits from BaseModel."""

from models.base_model import BaseModel

class City(BaseModel):
    """Class for managing city objects within the HBNB project.
    
    Attributes:
        state_id (str): The ID of the state a city belongs to.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
