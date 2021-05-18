from common import *
from . import Component
class Camera(Component):

    def __init__(self):
        Component.__init__(self)

        self.cap = None
        self.find_camera()

        self.cap.set(3, 1000)
        self.cap.set(4, 750)
        
    def find_camera(self):
        src = int(input('Camera device number (0 -> 3): '))
        # src = 3
        self.cap = cv2.VideoCapture(src, cv2.CAP_DSHOW)

        if self.cap.isOpened() and self.cap.read()[0]:
            ok('Connected to camera ' + str(src))
        else:
            fail('Cannot connect to camera !')

    def process(self):
        _, self.app.debug_image = self.cap.read()
        self.app.image = cv2.cvtColor(self.app.debug_image, cv2.COLOR_BGR2RGB)

    def shutdown(self):
        self.cap.release()