from threading import Thread, Timer
import webbrowser
from app import Application
import os
from server import Server
from threading import Thread
import httpwatcher

def run_app(app):
    while not app.stopped: 
        app.process()
        app.debug()

    app.shutdown()

def open_browser():
    webbrowser.open('http:/localhost:8080/app/explore')

def serve_file():
    Timer(1, open_browser).start()
    httpwatcher.watch(os.path.realpath('./static'), open_browser=False, port=8080, watch_paths=[])

if __name__ == '__main__':
    app = Application(name="FocusOP - qninh")
    server = Server(5000,
        static = os.path.realpath('./static'),
        fop    = os.path.realpath('./fops')
    )

    thread1 = Thread(target=run_app, args=(app,))
    thread1.start()

    thread2 = Thread(target=serve_file)
    thread2.start()

    server.start()