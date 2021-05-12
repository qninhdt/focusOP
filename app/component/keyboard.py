from common import *
from . import Component

class Keyboard(Component):

    def __init__(self):
        Component.__init__(self)
        self.pressed_key = []

    def process(self):
        self.pressed_key = cv2.waitKey(1)
        if self.pressed_key == Key.ESCAPE:
            self.app.stopped = True