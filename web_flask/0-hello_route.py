#!/usr/bin/python3
""" Script to start a Flask web app """

from flask import Flask

""" Creacion de instancia de la aplicación Flask """ 
app = Flask(__name__)
app.url_map.strict_slashes = False

""" Definir la ruta principal ("/") con el mensaje "Hello HBNB!" """
@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    Configurar la aplicación para que escuche en 0.0.0.0 en el puerto 5000
    """
    app.run(host='0.0.0.0', port=5000)
