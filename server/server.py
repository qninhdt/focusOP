from common import *
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS
from threading import Thread
import glob, os
class Server:

    def __init__(self, port, static, fop):
        self.port = port
        self.fop = fop
        self.static = static
        self.flask = Flask(__name__)

        CORS(self.flask)
        
        self.socket = SocketIO(self.flask, cors_allowed_origins='*')

        @self.flask.route('/')
        def home():
            return send_from_directory(self.static, 'index.html')

        @self.flask.route('/static/<filename>')
        def static_file(filename):
            return send_from_directory(self.static, filename)

        @self.socket.on('get_fops')
        def send_fops(_):
            os.chdir(self.fop)
            files = []
            for file in glob.glob("*.fop"):
                files.append(file)

            return files
        
        @self.socket.on('get_fop')
        def send_fop(filename):
            file = open(self.fop + "/" + filename, 'r', encoding="utf-8") 
            return file.read()

        @ee.on('new_hand_type')
        def new_hand_type(hand_type):
            self.socket.emit("new_hand_type", hand_type)

        @ee.on('new_hand_dir')
        def new_hand_dir(hand_dir):
            self.socket.emit("new_hand_dir", hand_dir)

        @ee.on('cursor')
        def cursor(point):
            self.socket.emit('cursor', point)

    def start(self):
        thread = Thread(target=self.socket.run, args=(self.flask,), kwargs={"port": self.port})
        thread.start()