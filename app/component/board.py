from common import *
from .component import Component

class Board(Component):

    def __init__(self):
        self.cursor = None

    def process(self):
        self.rect = 100, 100, 400, 300