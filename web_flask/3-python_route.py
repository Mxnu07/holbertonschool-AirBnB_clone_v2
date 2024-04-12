#!/usr/bin/python3
""" Script to start a Flask web app """

from flask import Flask
from urllib.parse import unquote_plus

""" Creacion de instancia de la aplicación Flask """
app = Flask(__name__)

""" Definir la ruta principal ("/") con el mensaje "Hello HBNB!" """


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    text = unquote_plus(text.replace('_', ' '))
    return (f"C {text}")


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    text = unquote_plus(text.replace('_', ' '))
    return (f"Python {text}")


if __name__ == '__main__':
    """
    Configurar la aplicación para que escuche en 0.0.0.0 en el puerto 5000
    """
    app.run(host='0.0.0.0', port=5000)
