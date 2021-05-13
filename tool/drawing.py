import cv2
global_font = cv2.FONT_HERSHEY_COMPLEX_SMALL
RED = (60, 76, 231)
GREEN = (113, 204, 46)
BLUE = (219, 152, 53)
YELLOW = (15, 196, 241)
ORANGE = (34, 126, 230)
WHITE = (241, 240, 236)
BGREEN = (156, 188, 26)
DGREEN = (96, 174, 39)
PURPLE = (182, 89, 155)
BLACK = (54, 52, 45)

def draw_text(image, text, pos, size=1, color=WHITE, thichness=None):
    cv2.putText(image, text, pos, global_font, size, color, thichness)

def draw_circle(image, pos, radius, color, thickness=-1):
    cv2.circle(image, (int(pos[0]), int(pos[1])), radius, color, thickness)

def draw_lines(image, points, color, thichness=None):
    for i in range(len(points) - 1):
        cv2.line(image, (int(points[i][0]), int(points[i][1])), (int(points[(i + 1)][0]), int(points[(i + 1)][1])), color, thichness)


def draw_transparent_rect(image, box, color, alpha):
    x, y, w, h = box
    overlay = image.copy()
    cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)
    image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    return image


FINGERS = [
 [
  4, 3, 2, 1],
 [
  8, 7, 6, 5],
 [
  12, 11, 10, 9],
 [
  16, 15, 14, 13],
 [
  20, 19, 18, 17]]
PALM = [
 0, 1, 5, 9, 13, 17, 0]

def draw_hand(image, points, states):
    for i, f in enumerate(FINGERS):
        color = BLUE if states[i] else BGREEN
        if i == 0:
            color = ORANGE if states[0] else YELLOW
        finger_points = [points[j] for j in FINGERS[i]]
        draw_lines(image, finger_points, color, thichness=2)
    else:
        palm_points = [points[j] for j in PALM]
        draw_lines(image, palm_points, BGREEN, 2)