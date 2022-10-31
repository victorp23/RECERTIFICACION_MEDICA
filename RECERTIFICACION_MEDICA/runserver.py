"""
This script runs the RECERTIFICACION_MEDICA application using a development server.
"""

from os import environ
from RECERTIFICACION_MEDICA import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '10.129.180.129')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
