#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, obj=None):
        """Returns a dictionary of models currently in storage"""
        ret = {}
        if obj:
            obj_name = obj.__name__
            for model in FileStorage.__objects:
                model_name = model.split(".")[0]
                if model_name == obj_name:
                    ret[model] = FileStorage.__objects[model]
            return (ret)
        return (FileStorage.__objects)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
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
            sp_all = self.all()
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    if key in sp_all:
                        sp_all[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj if it exists in the __objects attribute"""
        if obj is not None:
            key = "{:s}.{:s}".format(type(obj).__name__, obj.id)
            if key in FileStorage.__objects:
                del (FileStorage.__objects[key])
