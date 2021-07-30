from common import *
from . import Component
import device 

class Camera(Component):

    def __init__(self):
        Component.__init__(self)

        self.cap = None

    def open_camera(self,index):
        # print("Connect to camera ",index)
        self.cap = cv2.VideoCapture(index)
        self.cap.set(3, 1000)
        self.cap.set(4, 750)

    def process(self):
        if self.cap is not None:
            _, self.app.debug_image = self.cap.read()
            self.app.image = cv2.cvtColor(self.app.debug_image, cv2.COLOR_BGR2RGB)

    def shutdown(self):
        self.cap.release()