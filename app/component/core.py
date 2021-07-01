from common import *
from .component import Component

class Core(Component):

    def __init__(self):
        self.point_history = deque(maxlen=16)

    def process(self):
        hand = get('hand')
        
        if hand is not None and hand.hand_type == hand.PEACE:
            self.point_history.append(hand.index_point)

            point_history = list(filter(lambda p: p is not None, self.point_history))
            x, y, w, h = bounding_rect(point_history)
         
            first = point_history[0]
            last  = point_history[-1]
  
            if w > 100:
                if first[0] < last[0]:
                    set('hand_dir', 'left')
                else:
                    set('hand_dir', 'right')
            elif h > 75:
                if first[1] < last[1]:
                    set('hand_dir', 'up')
                else:
                    set('hand_dir', 'down')
   
        else:
            set('hand_dir', None)
            self.point_history.clear()
    
    def debug(self):
        for i, p in enumerate(self.point_history):
            if p is not None:
                draw_circle(self.app.debug_image, p, 3, GREEN, 1)