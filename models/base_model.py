#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    class BaseModel:
        """A base class for all hbnb models"""

        id = Column(String(60), unique=True, nullable=False,
                    primary_key=True, default=str(uuid.uuid4()))
        created_at = Column(DateTime,
                            default=datetime.utcnow(), nullable=False)
        updated_at = Column(DateTime,
                            default=datetime.utcnow(), nullable=False)

        def to_dict(self):
            """Convert instance into dict format"""
            dictionary = {}
            dictionary.update(self.__dict__)
            dictionary.update({'__class__':
                              (str(type(self)).split('.')[-1]).split('\'')[0]})
            dictionary['created_at'] = self.created_at
            dictionary['updated_at'] = self.updated_at
            key = "_sa_instance_state"
            if key in dictionary:
                del (dictionary[key])
            return dictionary
else:
    class BaseModel:
        def __init__(self, *args, **kwargs):
            """Instatntiates a new model"""
            if not kwargs:
                from models import storage
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            else:
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' in kwargs:
                    kwargs['created_at'] = datetime.strptime(
                            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.created_at = datetime.now()
                if 'updated_at' in kwargs:
                    kwargs['updated_at'] = datetime.strptime(
                            kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.updated_at = datetime.now()
                if '__class__' in kwargs:
                    del kwargs['__class__']
                self.__dict__.update(kwargs)

        def __str__(self):
            """Returns a string representation of the instance"""
            cls = (str(type(self)).split('.')[-1]).split('\'')[0]
            return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

        def save(self):
            """Updates updated_at with current time when instance is changed"""
            from models import storage
            self.updated_at = datetime.now()
            storage.new(self)
            storage.save()

        def to_dict(self):
            """Convert instance into dict format"""
            dictionary = {}
            dictionary.update(self.__dict__)
            dictionary.update({'__class__':
                              (str(type(self)).split('.')[-1]).split('\'')[0]})
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
            key = "_sa_instance_state"
            if key in dictionary:
                del (dictionary[key])
            return dictionary

        def delete(self):
            """Deletes the current instances from the storage"""
            storage.delete(self)
