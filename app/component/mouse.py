import pyautogui
from threading import Thread
from common import *
from . import Component
from time import time

pyautogui.FAILSAFE = False

class Mouse(Component):

    def __init__(self):
        self.last_hand_type = None
        self.is_running = False
        self.last_time = time()
        
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.thread = Thread(target=(self._process))
            self.thread.start()

    def _process(self):        

        while True:

            hand = get('hand')
            hand_dir = get('hand_dir')
            cursor = self.app.board.cursor

            if hand_dir == 'down':
                pyautogui.scroll(500)
            elif hand_dir == 'up':
                pyautogui.scroll(-500)

            if self.app.stopped or hand is None or cursor is None:
                break

            x, y = cursor
            w, h = pyautogui.size()
            x = int(x * w)
            y = int(y * h)

            # 1 time / 1 sec
            curr = time()

            if curr - self.last_time > 1:
                if (hand.hand_type == hand.NICE or hand.hand_type == hand.CONTROL):
                    if self.last_hand_type == hand.OPEN:
                        pyautogui.press('right')
                        self.last_time = curr

                if (hand.hand_type == hand.CLOSE or hand.hand_type == hand.NICE):
                    if self.last_hand_type == hand.FOUR:
                        pyautogui.press('left')
                        self.last_time = curr
            
                if self.last_hand_type == hand.NICE and hand.hand_type == hand.CONTROL:
                    pyautogui.press("right")
                    self.last_time = curr

                if self.last_hand_type == hand.NICE and hand.hand_type == hand.ALO:
                    pyautogui.press("left")
                    self.last_time = curr

            if hand.hand_type == hand.LMAO and self.last_hand_type == hand.PEACE:
                pyautogui.doubleClick(x, y)

            if hand.hand_type == hand.ROCK and self.last_hand_type == hand.POINT:
                pyautogui.click(x, y)
            
            if hand.hand_type == hand.POINT or hand.hand_type == hand.PEACE or hand.hand_type == hand.CONTROL or hand.hand_type == hand.OPEN or hand.hand_type == hand.FOUR:
                pyautogui.moveTo(x, y)
      
                if hand.hand_type == hand.CONTROL and self.last_hand_type == hand.POINT:
                    pyautogui.mouseDown(x, y)
                elif hand.hand_type == hand.POINT and self.last_hand_type == hand.CONTROL:
                    pyautogui.mouseUp(x, y)

            self.last_hand_type = None if hand is None else hand.hand_type

        self.is_running = False