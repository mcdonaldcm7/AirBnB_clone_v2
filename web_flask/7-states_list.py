#!/usr/bin/python3
"""This module starts a simple Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Handles request directed to root path"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles request directed to the path /hbnb"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_path(text):
    """Handles request directed to the path /c/<text>"""
    return ("C {}".format(text.replace('_', ' ')))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_path(text):
    """
    Handles the request and the argument passed to the path
    /python/(<text>)
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<int:n>", strict_slashes=False)
def number_path(n):
    """
    Handles the request and the arguments, also ensuring the argument
    passed is a number
    """
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_templates_path(n):
    """
    Handles the request and the arguments, also ensuring the argument
    passed is a number. Displays a HTML page using render_template
    """
    return (render_template("5-number.html", n=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_path(n):
    """
    Handles the request and the arguments, also ensuring the argument
    passed is a number. Displays a HTML page using render_template depending
    on the value of n
    """
    return (render_template("6-number_odd_or_even.html", n=n))


@app.teardown_appcontext
def teardown(arg):
    """Removes the SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """
    Display a HTML page with the list of all State objects present in DBStorage
    sorted by name (A->Z)
    """
    states = storage.all(State)
    return (render_template("7-states_list.html", states=states))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
