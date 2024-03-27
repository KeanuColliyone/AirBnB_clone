#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import unittest
from models.city import City
from datetime import datetime
import os

class TestCity(unittest.TestCase):
    """Tests the functionality of the City class."""

    def setUp(self):
        """Set up test methods."""
        self.city = City()

    def test_instance(self):
        """Test if the instance belongs to class City."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City correctly inherits from BaseModel."""
        self.assertTrue(hasattr(City, "id"))
        self.assertTrue(hasattr(City, "created_at"))
        self.assertTrue(hasattr(City, "updated_at"))

    def test_attributes(self):
        """Test if City has attributes 'state_id' and 'name', and they're as expected."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_set_attributes(self):
        """Test setting City attributes."""
        self.city.state_id = "State_id_example"
        self.city.name = "Example City"
        self.assertEqual(self.city.state_id, "State_id_example")
        self.assertEqual(self.city.name, "Example City")

    def test_to_dict_city(self):
        """Test dictionary representation of City."""
        self.city.state_id = "State_id_test"
        self.city.name = "Test City"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], "State_id_test")
        self.assertEqual(city_dict['name'], "Test City")
        self.assertEqual(city_dict['__class__'], 'City')

    def tearDown(self):
        """Tear down test methods."""
        del self.city

    @classmethod
    def tearDownClass(cls):
        """Clean up files (if any) created by the tests."""
        try:
            os.remove("file.json")
        except Exception:
            pass

if __name__ == "__main__":
    unittest.main()

