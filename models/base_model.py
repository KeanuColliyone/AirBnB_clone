#!/usr/bin/python3
"""This script is the base model from which all other will inherit"""

import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: Unused, for future expansion.
            - **kwargs: Dict of key-value arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns the official string representation of the instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dict containing all values of the instance's __dict__."""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
