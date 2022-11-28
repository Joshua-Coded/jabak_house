#!/usr/bin/python3
"""User module for JOSHUA project"""

from models.base_model import BaseModel

class User(BaseModel):

    """ this class defines a user by various attributes"""
    email = ""
    password = ""
    first_name = ""
