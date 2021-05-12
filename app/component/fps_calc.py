from common import *
from . import Component

class FpsCalc(Component):

    def __init__(self, buffer_len=10):
        Component.__init__(self)
        self._start_tick = cv2.getTickCount()
        self._freq = 1000.0 / cv2.getTickFrequency()
        self._difftimes = deque(maxlen=buffer_len)

    def process(self):
        current_tick = cv2.getTickCount()
        different_time = (current_tick - self._start_tick) * self._freq
        self._start_tick = current_tick
        self._difftimes.append(different_time)

    def __call__(self):
        fps = 1000.0 / (sum(self._difftimes) / len(self._difftimes))
        fps_rounded = round(fps)
        return fps_rounded

    def debug(self):
        self.app.debug_image = draw_transparent_rect(self.app.debug_image, (0, 100,
                                                                            100,
                                                                            30), BLACK, 0.8)
        draw_text(self.app.debug_image, 'FPS:' + str(self()), (5, 120), 1, DGREEN, 1)