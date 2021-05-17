import cv2
import numpy as np

image = cv2.imread('screen.jpg')
cap = cv2.VideoCapture(3)

cap.set(3, 1000)
cap.set(4, 750)

kernel = np.ones((5,5),np.uint8)

while True: 
    _, image = cap.read()

    h, w, _ = image.shape

    lower = np.array([0,0,0], dtype = "uint8")
    upper = np.array([120,120,120], dtype = "uint8")

    mask = cv2.inRange(image, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    output = cv2.bitwise_and(image, image, mask=mask)

    contours , _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    squares = []
    square_pairs = []

    for contour in contours:
    
        approx = cv2.approxPolyDP(contour, 0.1 * cv2.arcLength(contour, True), True)

        # kiem tra 4 canh
        if len(approx) != 4:
            continue

        area = cv2.contourArea(contour)

        x, y, w, h = cv2.boundingRect(contour)
        ratio = w/h
        delta = abs(ratio - 1)

        if delta > 0.1:
            continue

        squares.append(contour)
    
    l = len(squares)
    for i in range(l-1):
        for j in range(i+1, l):
            a1 = cv2.contourArea(squares[i])
            a2 = cv2.contourArea(squares[j])

            rect1 = cv2.boundingRect(squares[i])
            rect2 = cv2.boundingRect(squares[j])

            size = rect1[3]

            sw = abs(rect1[0]-rect2[0]) + size
            sh = abs(rect1[1]-rect2[1]) + size

            if abs(a1/a2-1) < .2 and sh > 0 and abs(sw/sh-16/9) < .2:
                print(sw/sh)
                square_pairs.append((squares[i], squares[j]))

    for sq1, sq2 in square_pairs:
        x, y, w, h = cv2.boundingRect(sq1)
        cv2.rectangle(output, (x, y), (x+w, y+h), (255, 0, 0), 2)

        x, y, w, h = cv2.boundingRect(sq2)
        cv2.rectangle(output, (x, y), (x+w, y+h), (255, 0, 0), 2)

    h, w, c = output.shape
    output = cv2.resize(output, (int(w/2), int(h/2)))
    cv2.imshow('Lmao 1', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()