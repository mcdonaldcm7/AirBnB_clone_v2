#!/usr/bin/python3
"""
This module starts a simple flask application and configures it to listen on
0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown(arg):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Fetches the State, City, and Amenity objects to be rendered dynamically in
    the 10-hbnb_filters.html
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return (render_template("10-hbnb_filters.html",
                            states=states, amenities=amenities))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
