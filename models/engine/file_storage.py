#!/usr/bin/python3
""" this module defines a class to manage file storage for joshua project """

import json


class FileStorage:
    """ this class manage storage of joshua models in JSON format"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ returns a dictionary of models current in storage"""
        return FileStorage.__objects
    
    def new(self, obj):
        """ adds new object to storage to file """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ saves new object to dictionary file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp,f)
    
    def reload(self):
        """Reload storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass