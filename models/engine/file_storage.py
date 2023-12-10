#!/usr/bin/python3
#file_storage.py

""" Define FileStorage"""

import json
import os
import datetime

class FileStorage:
    """
    Class that defines file storage

    Args:
    __file_path (string): path to the JSON file
    __objects (dictionary): store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects if path exists else exists"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                json_obj = json.load(f)
                class_name = json_obj[key]["__class__"]
                new_object = classes[class_name](**json_obj[key])
                self.__objects[key] = new_object
        except FileNotFoundError:
            pass
