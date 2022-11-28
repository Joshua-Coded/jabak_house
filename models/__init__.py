#!/usr/bin/python3
""" this module instantiates an object of class FILESTORAGE"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()