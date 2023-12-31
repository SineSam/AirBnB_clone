#!/usr/bin/python3
# base_model.py
"""Defindes base model"""


from datetime import datetime
import uuid
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialise instance attributes

        Args:
        *args (list): arguments
        **kwargs (dictionary): Key values in args
        """
        if kwargs is not None and kwargs is not {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], isoformat)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], isoformat)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
