#!/usr/bin/python3

"""Defines a base class BaseModel"""
import uuid
import datetime


class BaseModel:
    """Defines all common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """Runs on instantiation of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Overwrites the inbuilt __str__ method

        Returns:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
