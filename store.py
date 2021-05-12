import cv2
from threading import Lock

def get_tick():
    return cv2.getTickCount() / cv2.getTickFrequency()


data = {'image':None,
 'debug_image':None,
 'hand':None,
 'last_tick':0,
 'dtime':None}
lock = Lock()

def get(key):
    return data[key]


def set(key, val):
    lock.acquire()
    if key in ('hand', ):
        dtime = None
        if val is None and data['hand'] is not None:
            dtime = get_tick() - data['last_tick']
        else:
            if val is not None and data['hand'] is None:
                data['last_tick'] = get_tick()
            else:
                if val is not None and data['hand'].hand_type != val.hand_type:
                    dtime = get_tick() - data['last_tick']
                    data['last_tick'] = get_tick()
        data['dtime'] = dtime
    data[key] = val
    lock.release()