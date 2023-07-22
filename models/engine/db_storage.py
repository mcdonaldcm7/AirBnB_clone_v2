#!/usr/bin/python3
"""This module contains the definition for the DBStorage class which handles
the ORM operations we want to perform and gives us an abstracted method of
swapping between File Storage and Database Storage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """
    This class integrates the ORM concept into this project by using the
    SQLAlchemy library to make queries to the database and perform other
    file storage operations
    """
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        psswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST") #localhost
        db = os.getenv("HBNB_MYSQL_DB")
        is_test = True if os.getenv("HBNB_ENV") == "test" else False
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost/{}".format(
                    user, psswd, db),
                pool_pre_ping=True
                )

    def all(self, cls=None):
        """
        Make a query on the current database session all objects depending of
        the class name (argument cls)
        """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                "State": State, "User": User, "Place": Place,
                "City": City, "Amenity": Amenity, "Review": Review
                }
        dictionary = {}
        if cls is None:
            for class_name in classes:                
                objects = self.__session.query(classes[class_name]).all()
                printed = False
                for obj in objects:
                    if not printed:
                        print("---------In Loop-----------")
                    printed = True
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    print("Key is {}".format(key))
                    dictionary[key] = obj
        else:
            objects = self.__session.query(classes[cls]).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dictionary[key] = obj
        return (dictionary)

    def new(self, obj):
        """Add obj to the current database"""
        self.__session.add(obj)

    def save(self):
        """Commits all the changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.review import Review
        from models.place import Place
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the class session"""
        DBStorage.__session.close()
