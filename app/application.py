from app.component import board
from app.component.board import Board
from common import *
from .component import *

class Application:

    def __init__(self, name):
        self.name = name
        self.debug_image = None
        self.image = None
        self.camera = Camera()
        self.hand_detector = HandDetector()
        self.board = Board()
        self.keyboard = Keyboard()
        self.fps = FpsCalc()
        self.core = Core()
        self.mouse = Mouse()

        self.components = [
            self.camera,
            self.hand_detector,
            self.core,
            self.board,
            self.keyboard,
            self.mouse,
            self.fps
        ]
        self.stopped = False
        self.inject()
        self.init()

    def inject(self):

        def _inject(c):
            c.app = self

        [_inject(c) for c in self.components]

    def init(self):
        [c.init() for c in self.components]

    def process(self):
        [c.process() for c in self.components]

    def debug(self):
        [c.debug() for c in self.components]

        h, w, _ = self.debug_image.shape
        # self.debug_image = cv2.resize(self.debug_image, (int(w/2), int(h/2)))
        cv2.setMouseCallback(self.name, self.board.click)
        cv2.imshow(self.name, self.debug_image)

    def shutdown(self):
        [c.shutdown() for c in self.components]
        cv2.destroyAllWindows()
        warn('Shutdown !!')
        reset_color()