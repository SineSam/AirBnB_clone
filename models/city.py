#!/usr/bin/python3
#city.py

"""defines City class"""
import models
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """Attributes of City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialises city"""
        super().__init__(*args, **kwargs)
