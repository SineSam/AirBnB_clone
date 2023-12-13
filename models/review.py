#!/usr/bin/python3
"""
Define Review Class
"""

from models.base_mode import BaseModel


class Review(BaseMode):
    """Attributes of Review class"""
    place_id = ""
    user_id = ""
    text = ""
