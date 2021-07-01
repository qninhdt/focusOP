from math import dist
from common import *
import mediapipe
from . import Component
from app.lib.hand import Hand

class HandDetector(Component):
    lib_mphand = mediapipe.solutions.hands

    def __init__(self):
        self.result = None
        self.created_tflite = False
        self.mphand = self.lib_mphand.Hands(min_detection_confidence=0.75,
          min_tracking_confidence=0.5,
          max_num_hands=1)

    def _mp_process(self):
        self.app.image.flags.writeable = False
        self.result = self.mphand.process(self.app.image)
        self.app.image.flags.writeable = True

    def process(self):
        self._mp_process()
        if self.result.multi_hand_landmarks:
            self._preprocess_result()

        else:
            set('hand', None)

    @property
    def has_hand(self):
        return get('hand') is not None

    def _preprocess_result(self):
        lmss = self.result.multi_hand_landmarks
        rects = self.result.hand_rects
        hands = self.result.multi_handedness
        h, w, _ = self.app.image.shape
        for lms, rect, handn in zip(lmss, rects, hands):
            landmarks = np.array([(lm.x * w, lm.y * h) for lm in lms.landmark])
            hand = Hand(landmarks, handn.classification[0].label[0:], rect)
            hand.recognize()
            set('hand', hand)

    def debug(self):
        image = self.app.debug_image
        hand = get('hand')
        image = draw_transparent_rect(image, (0, 0, 100, 100), WHITE, 0.5)
        image = draw_transparent_rect(image, (0, 130, 100, 30), BLACK, 0.5)
        if hand is not None:
            draw_hand(image, hand.landmarks, hand.states)
            draw_hand(image, hand.points * 100, hand.states)
            draw_text(image, str(hand.get_hand_type_label()), (5, 150), 1, RED, 2)
        self.app.debug_image = image