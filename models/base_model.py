#!/usr/bin/python3
"""
    import module
"""
from datetime import datetime
import uuid
import datetime


"""
    Base class file
"""


class BaseModel:
    """
        base class of the console
    """
    def __init__(self, id, created_at, updated_at):
        """
            initiate the id of an instance with the data time
            args:
                id: the identification of the instance
                created_at: the current datetime when an instance is created
                updated_at: the current datetime when an instance is created
                    and it will be updated when an object is changed
        """
        self.id = str(uuid.uuid4(id))
        self.created_at = datetime.datetime(created_at)
        self.updated_at = updated_at

    @classmethod
    def __str__(cls, self):
        """
            return a string with the information of the object
        """
        return f"[{cls.__name__}] ({self.id}) {self.__dict__}"

    def __save__(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        return datetime.datetime(self.updated_at)

    def to_dict(cls, self):
        """
            returns a dictionary containing all keys/values of
            __dict__ of the instance 
        """
        dict = {"my_number": cls.__name__,
                "name": cls.__name__,
                "created_at": self.created_at,
                "updated_at": self.updated.at,
                "id": self.id}
        return dict



