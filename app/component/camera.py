from common import *
from . import Component

class Camera(Component):

    def __init__(self, src=0):
        Component.__init__(self)
        self.cap = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        self.cap.set(3, 1000)
        self.cap.set(4, 750)
        if self.cap.isOpened():
            ok('Connected to the camera')
        else:
            fail('Cannot connect to the camera')
    def process(self):
        _, self.app.debug_image = self.cap.read()
        self.app.image = cv2.cvtColor(self.app.debug_image, cv2.COLOR_BGR2RGB)

    def shutdown(self):
        self.cap.release()