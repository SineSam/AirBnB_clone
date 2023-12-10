#!/user/bin/python3
#user.py

"""defines the user class"""
import models
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Defines the user attributes

    Args:
    email (string): User email address
    password (string): User password
    first_name (string): User name
    last_name (string): User surname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""


    def __init__(self, *args, **kwargs):
        """Initialise user"""
        super().__init__(*args, **kwargs)
