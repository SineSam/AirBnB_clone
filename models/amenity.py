#!/usr/bin/python3
#amenity.py

"""Defines Amenity class"""

class Amenity(BaseModel, Base):
    """Attributes of Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init__(*args, **kwargs)
