from common import *
from flask import Flask, send_from_directory
from flask_socketio import SocketIO

class Server:

    def __init__(self, port, static):
        self.port = port
        self.static = static
        self.flask = Flask(__name__)
        self.socket = SocketIO(self.flask)

        @self.flask.route('/')
        def home():
            return send_from_directory(self.static, 'index.html')

        @self.flask.route('/<path:filename>')
        def static_file(filename):
            return send_from_directory(self.static, filename)

    def start(self):
        self.socket.run((self.flask), port=(self.port))