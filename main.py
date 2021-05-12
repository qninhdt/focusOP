from app import Application

app = Application(name="lmao")

while not app.stopped:
    app.process()
    app.debug()

app.shutdown()