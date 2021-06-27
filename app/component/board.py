from common import *
from .component import Component
import cv2, time

class Board(Component):

    def __init__(self):
        self.cursor = None
        self._cursor = None
        self.lower = np.array([0,0,0], dtype = "uint8")
        self.upper = np.array([80 ,80, 80], dtype = "uint8")
        self.rect = None

        self.squares = None
        self.last = 0
        self.is_locked = False

    def process(self):
        now = time.time()

        if self.rect is None:
            h, w, c = self.app.image.shape
            self.rect = 0, 0, w, h

        if not self.is_locked and (now - self.last > 1 or self.last == 0):
            # TWO SQUARES 
            kernel = np.ones((5,5),np.uint8)

            mask = cv2.inRange(self.app.debug_image, self.lower, self.upper)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
           
            contours , _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            squares = []

            for contour in contours:
                approx = cv2.approxPolyDP(contour, 0.1 * cv2.arcLength(contour, True), True)
                # kiem tra 4 canh
                if len(approx) != 4:
                    continue

                x, y, w, h = cv2.boundingRect(contour)
                ratio = w/h
                delta = abs(ratio - 1)

                if delta > 0.15:
                    continue

                squares.append(contour)
                #cv2.rectangle(self.app.debug_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            l = len(squares)
            for i in range(l-1):
                for j in range(i+1, l):
                    a1 = cv2.contourArea(squares[i])
                    a2 = cv2.contourArea(squares[j])

                    rect1 = cv2.boundingRect(squares[i])
                    rect2 = cv2.boundingRect(squares[j])

                    size = (rect1[2]+rect1[3]+rect2[2]+rect2[3])/4

                    sw = abs(rect1[0] - rect2[0]) 
                    sh = abs(rect1[1] - rect2[1]) 

                    sx = min(rect1[0], rect2[0])
                    sy = min(rect1[1], rect2[1])

                    sx -= size/2
                    sy -= size/2

                    sw += size*2
                    sh += size*2
                    
                    h, w, c = self.app.debug_image.shape

                    if abs(max(a1,a2)/min(a1,a2)-1.2) < .3 and sh > 0:
                        if abs(sw/sh-16/9) < .5 and sh*1.5 > h and sw*1.5 > w:
                            if abs(sw/size-50) < 100:
                                self.squares = [squares[i], squares[j]]
                                self.rect = int(sx), int(sy), int(sw), int(sh)
                                self.last = now
                                break

        # CURSOR
        hand = get('hand')

        x, y, w, h = self.rect

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

        if self.squares is not None:
            sq1, sq2 = self.squares
            x, y, w, h = cv2.boundingRect(sq1)
            cv2.rectangle(self.app.debug_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

            x, y, w, h = cv2.boundingRect(sq2)
            cv2.rectangle(self.app.debug_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        draw_text(self.app.debug_image, 'Locked' if self.is_locked else 'Unlocked', (self.rect[0], self.rect[1]-10), 1, ORANGE)
