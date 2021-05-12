import pyautogui
from threading import Thread, Lock
from common import *
from . import Component

class Mouse(Component):

    def __init__(self):
        self.last_hand_type = None
        self.thread = Thread(target=(self._process))
        self.lock = Lock()

    def init(self):
        self.thread.start()

    def _process(self):
        while not self.app.stopped:
            self.lock.acquire()
            hand = get('Right')
            if hand:
                x, y = hand.index_point
                ih, iw, _ = self.app.image.shape
                w, h = pyautogui.size()
                x = int(x * w / iw)
                y = int(y * h / ih)
                if hand.hand_type == hand.POINT or hand.hand_type == hand.CONTROL:
                    pyautogui.moveTo(x, y)
                    if hand.hand_type == hand.CONTROL and self.last_hand_type == hand.POINT:
                        pyautogui.mouseDown(x, y)
                    else:
                        if hand.hand_type == hand.POINT and self.last_hand_type == hand.CONTROL:
                            pyautogui.mouseUp(x, y)
                        else:
                            if hand.hand_type == hand.CONTROL and self.last_hand_type == None:
                                pyautogui.click(x, y)
                    self.last_hand_type = hand.hand_type
                else:
                    if self.last_hand_type == hand.CONTROL:
                        self.last_hand_type = None
                        pyautogui.mouseUp(x, y)
                    else:
                        self.last_hand_type = None
            self.lock.release()