#!/usr/bin/python3
""" City Module for HBNB project """
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import BaseModel, Base
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship

    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        __table_args__ = {"mysql_default_charset": "latin1"}
        state_id = Column(String(60), ForeignKey("states.id"), nullable=True)
        name = Column(String(128), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship(
                "Place", back_populates="cities", cascade="all, delete"
                )
else:
    from models.base_model import BaseModel

    class City(BaseModel):
        state_id = ""
        name = ""

        """ The city class, contains state ID and name """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
