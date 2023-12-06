#!/usr/bin/python3
# base_model.py

from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at

    def to_dict(self):
        my_dict = dict(id='str(self.id',
                created_at='self.created_at.isoformat()',
                updated_at='self.updated_at.isoformat')
        return my_dict
