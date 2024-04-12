#!/usr/bin/python3
""" Script that stars Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
""" module to List cities by states """


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def close_session(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
