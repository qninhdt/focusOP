from gevent.threading import Thread
from app import Application
import os
from server import Server
from threading import Thread

def run_app(app):
    while not app.stopped: 
        app.process()
        app.debug()

    app.shutdown()

if __name__ == '__main__':
    app = Application(name="lmao")
    server = Server(5000,
        static = os.path.realpath('./static'),
        fop    = os.path.realpath('./fops')
    )

    thread = Thread(target=run_app, args=(app,))
    thread.start()

    server.start()