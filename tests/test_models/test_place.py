#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Tests the functionality of the Place class."""

    def setUp(self):
        """Set up test methods."""
        self.place = Place()

    def test_instance(self):
        """Test if the instance belongs to class Place."""
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """Test if Place correctly inherits from BaseModel."""
        self.assertTrue(hasattr(Place, "created_at"))
        self.assertTrue(hasattr(Place, "updated_at"))

    def test_attributes(self):
        """Test if Place has the correct attributes and they are initialized."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def tearDown(self):
        """Tear down test methods."""
        del self.place

if __name__ == "__main__":
    unittest.main()

