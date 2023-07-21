#!/usr/bin/python3
""" City Module for HBNB project """
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import BaseModel, Base
    from models.state import State
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship

    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=True)
        name = Column(String(128), nullable=False)
        state = relationship("State", back_populates="cities")
else:
    from models.base_model import BaseModel

    class City(BaseModel):
        state_id = ""
        name = ""

        """ The city class, contains state ID and name """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
