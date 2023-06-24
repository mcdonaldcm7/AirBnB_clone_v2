#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = None

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
                "City", back_populates="state", cascade="all, delete"
                )
    else:
        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals to current
            State.id
            """
            from models import storage
            state_instances = storage.all(State)
            state_city = [
                    state for state in state_instances.values()
                    if state.state_id == self.id
                    ]
            return (state_city)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        super().__init__(*args, **kwargs)
