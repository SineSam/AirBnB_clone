#!/usr/bin/python3
"""defins State class"""

import models
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """Public class attribute representing the state"""
    name = ""

    def __init__(self, *self, *args, **kwargs):
        """Initialise state"""
        super().__init__(*args, **kwargs)
