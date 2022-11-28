#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class test_Review(test_basemodel):
    """Test"""

    def __init__(self, *args, **kwargs):
        """Create"""
        super().__init(self, *args, **kwargs)
        self.name = "Review"
        self.value = Review

    
    def test_place_id(self):
        """Create"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Create"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Create"""
        new = self.value()
        self.assertEqual(type(new.text), str)