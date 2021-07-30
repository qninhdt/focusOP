from threading import Thread, Timer
import webbrowser
from app import Application
import os
from server import Server
from threading import Thread
import httpwatcher
from store import ee
import setting

def run_app(port):
    app = Application(name=setting.name,camera_port=port)
    while not app.stopped: 
        app.process()
        app.debug()

    app.shutdown()

def open_browser():
    webbrowser.open('http:/localhost:8080/app/device')

def serve_file():
    Timer(1, open_browser).start()
    httpwatcher.watch(os.path.realpath('./static'), open_browser=False, port=setting.public_port, watch_paths=[])

if __name__ == '__main__':
    server = Server(setting.api_port,
        static = os.path.realpath('./static'),
        fop    = os.path.realpath('./fops')
    )

    @ee.on("set_device")
    def set_device(port):
        print(port)
        thread1 = Thread(target=run_app,args=(port,))
        thread1.start()

    thread2 = Thread(target=serve_file)
    thread2.start()

    server.start()