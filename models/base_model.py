#!/usr/bin/python3

'''
BaseModel - written by Michael Mensah and Frimpong Rijkaard.
Module of all modules
'''
import models
import uuid
from datetime import datetime


time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():

    ''' Base class for all classes'''

    def __init__(self, *args, **kwargs):
        '''
            constructor for Base model class
            Args:
            id - string, assign with uuid when instance is created
            created_at - assign datetime when instance is created
            updated_at - assign datetime when instance is updated
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        '''
            string representation of a class
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        '''
            updates the public instance attribute updated_at with the current
            datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
            returns a dict containing all keys/values of __dict__ of the
            instance
        '''
        my_dict = self.__dict__
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
