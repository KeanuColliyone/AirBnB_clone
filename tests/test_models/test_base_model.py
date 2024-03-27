#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """Test the functionality of the BaseModel class."""

    def test_init_no_args(self):
        """Test initialization without arguments."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        datetime_now = datetime.now().isoformat()
        model = BaseModel(id="123", created_at=datetime_now, updated_at=datetime_now)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at.isoformat(), datetime_now)
        self.assertEqual(model.updated_at.isoformat(), datetime_now)

    def test_str(self):
        """Test string representation."""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(expected_str, str(model))

    def test_save(self):
        """Test the save method."""
        model = BaseModel()
        updated_at_before = model.updated_at
        model.save()
        updated_at_after = model.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    def test_to_dict(self):
        """Test conversion of instance attributes to dictionary for JSON."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertTrue("created_at" in model_dict)
        self.assertTrue("updated_at" in model_dict)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

    @classmethod
    def tearDownClass(cls):
        """Clean up files (if any) created by the test cases."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()

