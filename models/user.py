#!/usr/bin/python3
"""This module creates a User class that inherits from BaseModel."""
from models.base_model import BaseModel

class User(BaseModel):
    """Class for managing user objects.
    
    Attributes:
        email (str): The email address of the user.
        password (str): The password for the user account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
