#!/usr/bin/python3
""" Review module for the HBNB project """
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship
    from models.base_model import BaseModel, Base

    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = "reviews"
        __table_args__ = {"mysql_default_charset": "latin1"}
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
else:
    from models.base_model import BaseModel

    class Review(BaseModel):
        """ Review classto store review information """
        place_id = ""
        user_id = ""
        text = ""
