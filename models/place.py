#!/usr/bin/python3
""" Place Module for HBNB project """
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import BaseModel, Base
    from sqlalchemy import Column, String, Integer, Float, ForeignKey
    from sqlalchemy.orm import relationship

    class Place(BaseModel):
        """ A place to stay """
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        review = relationship(
                "Review", back_populates="place", cascade="all, delete"
                )
else:
    from models.base_model import BaseModel

    class Place(BaseModel):
        """ A place to stay """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        def __init__(self, *args, **kwargs):
            if kwargs:
                for key in kwargs:
                    if key == "__class__":
                        continue
                    else:
                        setattr(self, key, kwargs[key])
            super().__init__(*args, **kwargs)

        @property
        def review(self):
            """Returns the list of reviews"""
            from models import storage
            review_instances = storage.all(Review)
            place_reviews = [
                    review for review in review_instances.values()
                    if review.place_id == self.id
                    ]
            return (place_reviews)
