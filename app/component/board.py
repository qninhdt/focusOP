from common import *
from .component import Component

class Board(Component):

    def __init__(self):
        self.cursor = None
        self._cursor = None

    def process(self):
        self.rect = 150, 50, 600, 400
        x, y, w, h = self.rect
        hand = get('hand')

        if hand is not None:
            index_point = hand.index_point

            if is_inside_box(index_point, self.rect):
                self._cursor = index_point
                self.cursor = [
                    (self._cursor[0] - x)/w, 
                    (self._cursor[1] - y)/h
                ]
                ee.emit('cursor', { "point": self.cursor })
                self.app.mouse.start()
            else:
                self._cursor = None 
                self.cursor = None               

    def debug(self):
        draw_rect(self.app.debug_image, self.rect, BLUE, 2)

        if self._cursor is not None:
            draw_circle(self.app.debug_image, self._cursor, 4, YELLOW, -1)