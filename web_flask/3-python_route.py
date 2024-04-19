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
def c_text(text):
    text = text.replace('_', ' ')
    return "c {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
