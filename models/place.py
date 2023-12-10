#!/usr/bin/python3
# place.py
"""Defines Place class"""
import models
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """Attributes of Place class

    Args:
    city_id (string): the id of the city
    user_id (string) : The id of the user
    name (string): the name of the place
    description (string) : the description of the location
    number_rooms (int): the number of rooms
    number_bathrooms (int): the number of bathrooms
    max_guests (int): the maximum number of guests
    price_by_night (int): the price per night
    latitude (float): the latitude of the location
    longitude (float): the logatude of the location
    amenity_ids (list of strings) : the list of Amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialise Place"""
        super().__init__(*args, **kwargs)
