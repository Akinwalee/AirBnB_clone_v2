#!/usr/bin/python3
"""A simple Flask application"""

from flask import Flask
from markupsafe import escape

app = Flask('__name__')


@app.route('/')
def index():
    """Function for index route"""

    return ('Hello HBNH!')


@app.route('/hbnb')
def hbnb():
    """Function to display HBNB"""

    return ('HBNB')


@app.route('/c/<text>')
def display_c():

    """Function for C route"""

    return (f'C {escape(text.replace("_", " "))}')


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
