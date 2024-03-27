#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

import unittest
from models.amenity import Amenity
from datetime import datetime
import os

class TestAmenity(unittest.TestCase):
    """Tests the functionality of the Amenity class."""

    def setUp(self):
        """Set up test methods."""
        self.amenity = Amenity()

    def test_instance(self):
        """Test if the instance belongs to class Amenity."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity correctly inherits from BaseModel."""
        self.assertTrue(hasattr(Amenity, "id"))
        self.assertTrue(hasattr(Amenity, "created_at"))
        self.assertTrue(hasattr(Amenity, "updated_at"))

    def test_attributes(self):
        """Test if Amenity has attribute 'name' and it's as expected."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_set_attributes(self):
        """Test setting Amenity attributes."""
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_to_dict_amenity(self):
        """Test dictionary representation of Amenity."""
        self.amenity.name = "Wi-Fi"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Wi-Fi")
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def tearDown(self):
        """Tear down test methods."""
        del self.amenity

    @classmethod
    def tearDownClass(cls):
        """Clean up files (if any) created by the tests."""
        try:
            os.remove("file.json")
        except Exception:
            pass

if __name__ == "__main__":
    unittest.main()

