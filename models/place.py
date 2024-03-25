#!/usr/bin/python3
"""This module creates a Place class that inherits from BaseModel."""

from models.base_model import BaseModel

class Place(BaseModel):
    """Class for managing place objects within the application.
    
    Attributes:
        city_id (str): The city ID where the place is located.
        user_id (str): The user ID of the place's host.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price of the place for one night.
        latitude (float): The latitude of the place's location.
        longitude (float): The longitude of the place's location.
        amenity_ids (list): A list of Amenity IDs associated with the place.
    """
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
