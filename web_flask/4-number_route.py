#!/usr/bin/python3
"""
This script starts a Flask web application listening on 0.0.0.0, port 5000.
It defines a route that displays "Hello HBNB!" when accessed.
"""
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Route function for the root URL."""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def start():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")

@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
