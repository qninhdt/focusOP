from math import degrees, pi, sqrt, sin, cos, tan, acos
import cv2
import numpy as np

def calc_sin_cos(angle):
    c = cos(angle)
    s = sqrt(1-c**2)

    if angle < 0:
        s = -s

    return s, c

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def bounding_rect(points):
    x_min, y_min = points[0][0], points[0][1]
    x_max, y_max = points[0][0], points[0][1]

    for p in points:
        x_min, y_min = min(x_min, p[0]), min(y_min, p[1])
        x_max, y_max = max(x_max, p[0]), max(y_max, p[1])

    return x_min, y_min, x_max-x_min, y_max-y_min

def normalize_points(points, size):
    x, y, _, _ = bounding_rect(points)

    for p in points:
        p[0] -= x
        p[1] -= y
        p[0] /= size
        p[1] /= size

    return points

def rotate_points(points, angle):
    s, c = calc_sin_cos(angle)

    npoints = []

    for x, y in points:
        xnew = x * c - y * s
        ynew = x * s + y * c

        npoints.append([xnew, ynew])

    return npoints

def angle(a, b, c):
    ab = distance(a, b)
    bc = distance(b, c)
    ca = distance(c, a)

    cos_theta = (ab**2 + bc**2 - ca**2) / (2*ab*bc)

    return degrees(acos(cos_theta)) 