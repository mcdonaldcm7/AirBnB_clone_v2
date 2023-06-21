#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def get_cities(self):
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
