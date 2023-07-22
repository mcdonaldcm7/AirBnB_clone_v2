#!/usr/bin/python3
""" State Module for HBNB project """
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import BaseModel, Base
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
                "City", back_populates="state", cascade="all, delete"
                )
else:
    from models.base_model import BaseModel
    from models.city import City

    class State(BaseModel):
        def __init__(self, *args, **kwargs):
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)
            super().__init__(*args, **kwargs)

        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals to current
            State.id
            """
            from models import storage
            city_instances = storage.all(City)
            city_list = [
                    city for city in city_instances.values()
                    if city.state_id == self.id
                    ]
            return (city_list)
