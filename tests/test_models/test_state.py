#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State

class test_State(test_basemodel):
    """Test"""
    
    def __init__(self, *args, **kwargs):
        """Create"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)