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
        elif self.pressed_key == Key.L:
            self.app.board.is_locked = True
        elif self.pressed_key == Key.U:
            self.app.board.is_locked =  False