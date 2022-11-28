#!/usr/bin/python3
"" " """
from tests.test_models.test_base_model import test_basemodel
from models.city import City

class test_City(test_basemodel):
    """Test"""

    def __init__(self, *args, **kwargs):
        """Construct"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state id""" 
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)       