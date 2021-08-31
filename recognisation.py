import cv2
import time
from sliding_window import *


img = cv2.imread('test 10.png', cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = img.copy()
cv2.imshow('Original', img)
cv2.waitKey(0)
# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# thresh = cv2.bitwise_not(thresh1)
count = 0
winH, winW = 20, 20
texts, locations = [], []
scale = 1.5
for resized in pyramid(gray, scale):
    count += 1
    print(count)
    for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue

        # check(window, texts, locations, x, y, scale**count)

        clone = resized.copy()
        clone = cv2.cvtColor(clone,cv2.COLOR_GRAY2BGR)
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2,)
        cv2.imshow("Window", clone)
        cv2.waitKey(1)
        time.sleep(0.025)

# cv2.imshow('Gray', gray)
# cv2.imshow('Gaussian', gauss)
# cv2.imshow('Thresh', thresh)

# cv2.waitKey(0)
cv2.destroyAllWindows()
