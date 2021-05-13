from app import Application
import os
from server import Server

app = Application(name="lmao")
server = Server(5000,
    static = os.path.realpath('./static'),
    fop    = os.path.realpath('./fops')
)

server.start()

while not app.stopped: 
    app.process()
    app.debug()

app.shutdown()