import cv2
current_time = 0

def timer_start():
    global current_time
    current_time = cv2.getTickCount()


def timer_result():
    diff = cv2.getTickCount() - current_time
    return round(diff / cv2.getTickFrequency(), 2)