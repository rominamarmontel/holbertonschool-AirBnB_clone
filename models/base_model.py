#!/usr/bin/python3
"""
    import module
"""
from datetime import datetime
import uuid
from datetime import date


"""
    Base class file
"""


class BaseModel:
    """
        base class of the console
    """
    def __init__(self):
        """
            initiate the id of an instance with the data time
            args:
                id: the identification of the instance
                created_at: the current datetime when an instance is created
                updated_at: the current datetime when an instance is created
                    and it will be updated when an object is changed
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def __str__(self):
        """
            return a string with the information of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of
            __dict__ of the instance 
        """
        dict = {"updated_at": self.updated_at,
                "id": self.id,
                "created_at": self.created_at,}
        return dict



