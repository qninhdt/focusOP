from common import *

hand_type_labels = {11000:'CONTROL',
 11111:'OPEN',
 0:'CLOSE',
 1000:'POINT',
 1100:'PEACE',
 1110:'THREE',
 1111:'FOUR',
 100:'FUCK',
 1001:'ROCK',
 10000:'NICE',
 10001:'ALO',
 11001:'SPIDER',
 10002:'HEART',
 10003:'STRAIGHT',
 10004:'GUN',
 10005:'OK'}

class Hand:
    OPEN = 11111
    CLOSE = 0
    POINT = 1000
    PEACE = 1100
    THREE = 1110
    FOUR = 1111
    FUCK = 100
    ROCK = 1001
    NICE = 10000
    ALO = 10001
    SPIDER = 11001
    CONTROL = 11000
    HEART = 10002
    STRAIGHT = 10003
    GUN = 10004
    OK = 10005

    def __init__(self, landmarks, label, rect):
        self.landmarks = landmarks
        self.label = label
        self.rect = rect
        self.states = [False] * 5
        self.hand_type = None

    def preprocess(self):
        self.points = rotate_points(self.landmarks, -self.rect.rotation)
        self.points = normalize_points(self.points, max(2.5 * distance(self.points[0], self.points[5]), 2 * distance(self.points[6], self.points[5])))
        self.index_point = self.landmarks[8]

    def recognize(self):
        self.preprocess()
        self.states = [
         self._is_thumb_opened(),
         self._is_finger_opened(8, 150, 100, 0.5),
         self._is_finger_opened(12, 150, 100, 0.6),
         self._is_finger_opened(16, 150, 100, 0.5),
         self._is_finger_opened(20, 150, 100, 0.5)]
        self.hand_type = 0
        for i in range(len(self.states)):
            self.hand_type += self.states[i] * 10 ** (4 - i)
        else:
            if self.states[2]:
                if self.states[3]:
                    if self.states[4]:
                        if distance(self.points[4], self.points[8]) < 0.1:
                            self.hand_type = Hand.OK

    def get_hand_type_label(self):
        if self.hand_type in hand_type_labels:
            return hand_type_labels[self.hand_type]
        return 'Undefined'

    def _is_thumb_opened(self):
        a = distance(self.points[4], self.points[14])
        return a > 0.35

    def _is_finger_opened(self, tip, min_alpha, min_beta, min_d):
        alpha = angle(self.points[tip], self.points[(tip - 1)], self.points[(tip - 2)])
        beta  = angle(self.points[(tip - 1)], self.points[(tip - 2)], self.points[(tip - 3)])
        theta = angle(self.points[(tip - 2)], self.points[(tip - 3)], self.points[0])
        return alpha > min_alpha and beta > min_beta and theta > 120 and distance(self.points[tip], self.points[0]) > min_d

    def __str__(self):
        return self.get_hand_type_label()