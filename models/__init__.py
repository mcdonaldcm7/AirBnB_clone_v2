#!/usr/bin/python3
"""
This module instantiates an object depending on the value of the environment
variable 'HBNB_TYPE_STORAGE'.

if "HBNB_TYPE_STORAGE" == 'db':
    instantiate the class DBStorage
else:
    FileStorage

This 'switch' allows us to change storage type directly by using an
environment variable
"""
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
