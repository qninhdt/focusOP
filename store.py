import cv2
from threading import Lock
from pyee import BaseEventEmitter

ee = BaseEventEmitter()

def get_tick():
    return cv2.getTickCount() / cv2.getTickFrequency()


data = {
    'image':None,
    'debug_image':None,
    'hand':None,
    'last_tick':0,
    'dtime':None,
    'hand_dir': None
}
lock = Lock()

def get(key):
    return data[key]


def set(key, val):
    lock.acquire()

    if key == 'hand':
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

        if dtime is not None:
            label = None if val is None else val.get_hand_type_label()
            ee.emit("new_hand_type", { "label": label, "dtime": dtime })

        data['dtime'] = dtime

    elif key == 'hand_dir':
        if val != data['hand_dir']:
            ee.emit('new_hand_dir', data['hand_dir'])

    data[key] = val
    lock.release()